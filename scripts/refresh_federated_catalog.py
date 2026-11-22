#!/usr/bin/env python3
"""Refresh the six-account public repository catalogue from GitHub."""
import json, os, urllib.error, urllib.parse, urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"data"
ACCOUNTS=["HuffmanMainNode","PCakes303","HuffmanRepositories","midnightlolz31337","roberthuffman","Ryzean84"]
TOKEN=os.environ.get("GITHUB_TOKEN","")
NOW=datetime.now(timezone.utc)
STAMP=NOW.strftime("%Y-%m-%d")
VERIFIED=NOW.isoformat(timespec="seconds").replace("+00:00","Z")

def api_get(url):
    headers={"Accept":"application/vnd.github+json","X-GitHub-Api-Version":"2022-11-28","User-Agent":"Huffman-Public-Archive-Topology"}
    if TOKEN: headers["Authorization"]="Bearer "+TOKEN
    req=urllib.request.Request(url,headers=headers)
    try:
        with urllib.request.urlopen(req,timeout=45) as response: return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        raise RuntimeError("GitHub API HTTP "+str(exc.code)+" for "+url+": "+exc.read().decode("utf-8",errors="replace")) from exc

def load(path,default):
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else default

def dump(path,value):
    path.write_text(json.dumps(value,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")

account_path=DATA/"accounts.json"
ledger_path=DATA/"federated-repositories.json"
relationship_path=DATA/"cross-account-relationships.json"
old_accounts_doc=load(account_path,{})
old_ledger_doc=load(ledger_path,{})
old_relationships=load(relationship_path,{})
old_accounts={x["login"]:x for x in old_accounts_doc.get("accounts",[])}
old_records={x["full_name"]:x for x in old_ledger_doc.get("repositories",[]) if x.get("full_name")}
records=[]; account_rows=[]; fork_edges=[]

for login in ACCOUNTS:
    page=1; observed=[]
    while True:
        query=urllib.parse.urlencode({"type":"owner","sort":"full_name","direction":"asc","per_page":100,"page":page})
        batch=api_get("https://api.github.com/users/"+login+"/repos?"+query)
        if not isinstance(batch,list): raise RuntimeError("Unexpected repository response for "+login)
        observed.extend(batch)
        if len(batch)<100: break
        page+=1
    public=[r for r in observed if not r.get("private",False)]
    if not public: raise RuntimeError("No public repositories returned for "+login+"; refusing to publish.")
    tally={"public":len(public),"original_projects":0,"forks":0,"controlled_test_copies":0,"profiles":0}
    for r in public:
        full=r["full_name"]; old=old_records.get(full,{})
        fork=bool(r.get("fork"))
        classification=old.get("classification")
        if fork: classification="upstream_fork"
        elif classification not in ("profile","controlled_test_copy","portfolio_index"):
            classification="profile" if r["name"].lower()==login.lower() else "original_project"
        if classification=="profile": tally["profiles"]+=1
        elif classification=="controlled_test_copy": tally["controlled_test_copies"]+=1
        elif classification=="upstream_fork": tally["forks"]+=1
        else: tally["original_projects"]+=1
        parent=r.get("parent") or {}; source=r.get("source") or {}
        upstream=parent.get("full_name") or source.get("full_name")
        upstream_url=parent.get("html_url") or source.get("html_url")
        github_description=r.get("description")
        record={**old,
          "name":r["name"],"owner":login,"account":login,"full_name":full,
          "url":r.get("html_url") or "https://github.com/"+full,
          "fork":fork,"archived":bool(r.get("archived")),
          "default_branch":r.get("default_branch"),
          "description":old.get("description") or github_description,
          "github_description":github_description,
          "classification":classification,"evidence_level":"repository_metadata_verified",
          "created_at":r.get("created_at"),"updated_at":r.get("updated_at"),"pushed_at":r.get("pushed_at"),
          "language":r.get("language"),"license_spdx_id":(r.get("license") or {}).get("spdx_id"),
          "topics":r.get("topics") or [],"last_verified_at":VERIFIED}
        if fork and upstream:
            record["upstream"]=upstream
            record["upstream_url"]=upstream_url or "https://github.com/"+upstream
            fork_edges.append({"from":full,"to":upstream,"type":"github_fork","verified":True,"last_verified_at":VERIFIED})
        else:
            record.pop("upstream",None); record.pop("upstream_url",None)
        records.append(record)
    previous=old_accounts.get(login,{})
    account_rows.append({**previous,"login":login,"role":previous.get("role","Public account in the federated collection"),
      "url":"https://github.com/"+login,"public_repositories":tally["public"],
      "original_projects":tally["original_projects"],"forks":tally["forks"],
      "controlled_test_copies":tally["controlled_test_copies"],"profile_repositories":tally["profiles"],
      "last_verified_at":VERIFIED})

records.sort(key=lambda x:(x["account"].lower(),x["name"].lower()))
if len({x["full_name"] for x in records})!=len(records): raise RuntimeError("Duplicate full_name values detected.")
by_account={}
for a in account_rows:
    by_account[a["login"]]={"public":a["public_repositories"],"original_projects":a["original_projects"],
      "forks":a["forks"],"controlled_test_copies":a["controlled_test_copies"],"profiles":a["profile_repositories"]}
main=by_account["HuffmanMainNode"]
alts=[x for x in ACCOUNTS if x!="HuffmanMainNode"]
alternate={key:sum(by_account[x][key] for x in alts) for key in ("public","original_projects","forks","controlled_test_copies","profiles")}
portfolio_indexes=sum(1 for x in records if x["classification"]=="portfolio_index")
counts={"account_count":len(account_rows),"public_repositories":len(records),
 "original_project_repositories":sum(a["original_projects"] for a in account_rows),
 "upstream_forks":sum(a["forks"] for a in account_rows),
 "controlled_test_copies":sum(a["controlled_test_copies"] for a in account_rows),
 "profile_repositories":sum(a["profile_repositories"] for a in account_rows),"by_account":by_account,
 "main_account":{"public_repositories":main["public"],"original_projects":main["original_projects"],"upstream_forks":main["forks"],"profiles":main["profiles"]},
 "alternate_accounts":{"public_repositories":alternate["public"],"original_projects":alternate["original_projects"],"upstream_forks":alternate["forks"],"controlled_test_copies":alternate["controlled_test_copies"],"profiles":alternate["profiles"]}}
scope="All public repositories across the six configured accounts; private repositories are excluded."
common={"schema_version":"1.1.0","snapshot_date":STAMP,"last_verified_at":VERIFIED,"scope":scope,"counts":counts,"accounts":account_rows}
dump(account_path,common)
dump(ledger_path,{**common,"repositories":records})
relationships=old_relationships or {"schema_version":"1.0.0"}
relationships.update({"schema_version":"1.1.0","snapshot_date":STAMP,"fork_lineage":sorted(fork_edges,key=lambda x:x["from"])})
dump(relationship_path,relationships)

lines=["# Federated Public Repository Catalog","","Human-readable directory for the six-account public collection. Repository names link to canonical GitHub pages. The JSON ledger is the machine-readable source of record.","",
"## Collection at a glance","",f"- Snapshot: {STAMP}",f"- Last verified: {VERIFIED}",
f"- Accounts: {counts['account_count']}",f"- Public repositories: {counts['public_repositories']}",
f"- Original project repositories (including portfolio index): {counts['original_project_repositories']}",
f"- GitHub-confirmed upstream forks: {counts['upstream_forks']}",
f"- Controlled test copies: {counts['controlled_test_copies']}",f"- Profile repositories: {counts['profile_repositories']}","",
"## Navigate by account","","| Account | Public repositories | Collection role |","|---|---:|---|"]
for a in account_rows:
    role=a["role"].replace("|","\\|")
    lines.append(f"| [{a['login']}]({a['url']}) | {a['public_repositories']} | {role} |")
lines.extend(["","## Repository directory",""])
for a in account_rows:
    subset=[r for r in records if r["account"]==a["login"]]
    lines.extend([f"### [{a['login']}]({a['url']})","",a["role"],"",
      "| Repository | Classification | Project family | Description | Upstream |","|---|---|---|---|---|"])
    for r in subset:
        desc=r.get("description") or r.get("github_description") or "No description supplied; consult the repository README."
        desc=" ".join(str(desc).replace("|","\\|").split())
        family=str(r.get("family") or "Unclassified").replace("|","\\|")
        upstream=r.get("upstream")
        upstream_cell=f"[{upstream}]({r.get('upstream_url') or 'https://github.com/'+upstream})" if upstream else "Not applicable / not recorded"
        lines.append(f"| [{r['name']}]({r['url']}) | {r['classification'].replace('_',' ')} | {family} | {desc} | {upstream_cell} |")
    lines.extend(["",f"<sub>{len(subset)} repository records in this account section.</sub>",""])
lines.extend(["## Classification and evidence","",
"- Original project: GitHub reports fork=false; this does not prove authorship of every file.",
"- Upstream fork: GitHub reports fork=true; upstream is linked when GitHub exposes its parent/source.",
"- Controlled test copy: a separately tracked category, not counted as an original project.",
"- Profile: account landing page, not a standalone product.",
"- Portfolio index: this archive repository, counted with original project repositories for collection totals.",
"- Project family: discovery grouping only, not a runtime dependency.","",
"## Machine access","","- [Federated repository ledger](data/federated-repositories.json)",
"- [Account registry](data/accounts.json)","- [Cross-account relationships](data/cross-account-relationships.json)",
"- [Agent entrypoint](AGENT-ENTRYPOINT.md)","","## Freshness",
"",
"The scheduled GitHub Actions workflow refreshes public metadata daily and supports manual execution. A successful metadata refresh is not a source-code, security, or production-readiness audit.",""])
catalog=ROOT/"FEDERATED-CATALOG.md"
catalog.write_text("\n".join(lines),encoding="utf-8")
rows=[line for line in lines if line.startswith("| [") and any("| "+label+" |" in line for label in ("original project","upstream fork","controlled test copy","profile","portfolio index"))]
if len(rows)!=len(records): raise RuntimeError(f"Catalogue row count {len(rows)} != ledger count {len(records)}")
if sum(a["public_repositories"] for a in account_rows)!=len(records): raise RuntimeError("Account totals do not reconcile.")
if len(account_rows)!=6 or not records: raise RuntimeError("Unexpected account/repository count.")
if len(fork_edges)>counts["upstream_forks"]: raise RuntimeError("More upstream edges than fork records were generated.")
print(f"Refreshed {len(records)} public repositories across {len(account_rows)} accounts.")
print(f"Original-project bucket: {counts['original_project_repositories']}; forks: {counts['upstream_forks']}; test copies: {counts['controlled_test_copies']}; profiles: {counts['profile_repositories']}.")
