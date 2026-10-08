"""Build/verify the immutable AIChat 1.18.30 + SPP 5.10.10 release."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import zipfile
import build_trilingual_docs as docs
from verify_release import check_archive

ROOT = Path(__file__).resolve().parents[1]
NAME = 'AIChat_v1.18.30_SPP_v5.10.10'
TAG = 'AIChat-v1.18.30_SPP-v5.10.10'
ZIP = 'SatoneMod_AIChat_1.18.30_SPP_5.10.10_Windows_x64.zip'
MANIFEST = ROOT / 'releases' / (NAME + '.json')
PACKAGE = ROOT / 'packages' / NAME
BASE_NAME = 'SatoneMod_AIChat_1.18.28_SPP_5.10.8_Windows_x64.zip'
BASE = ROOT / 'packages/AIChat_v1.18.28_SPP_v5.10.8' / BASE_NAME
BASE_HASH = '5c13266e6ec9d1f7e775bb305d1734099b845acc91ecb27902c5290b9bb2f45e'
VERSIONS = {'AIChat': '1.18.30', 'SPP': '5.10.10'}
SOURCES = {'AIChat': '4cefab9c9bf64762a7d1c7a4ed6e081c8d13fd96', 'SPP': '7c113e04e68280fe9d0296b4ca6be51088b74732'}
TESTED = {'AIChat': '49b31f4177212f48ea1753351b4d3df65e97524a', 'SPP': '42a5cbfadc6a313740f0b24849c0045134f51b93'}
BINARIES = {'AIChat/AIChat.dll': 'ffdfe1ee9ec7a47ce2822baa6a2ba139afc10555a626baab59f590e477a33e68',
            'AIChat/AIChat.pdb': 'e2f1262d96417987a9a50b70412e725d2b21a4063f4398d748ddc61f0c37db3b',
            'SatonePromptProxy/SatonePromptProxy.exe': 'f9322676d55e8c3b5dd653e9d7179d72fc212c8f2c049ebc56f8aee562117beb'}

def sha(data):
    return hashlib.sha256(data).hexdigest()

def jb(value):
    return (json.dumps(value, ensure_ascii=False, indent=2)+'\n').encode('utf-8')

def gateway(prefix, page, title):
    return (f'# {title}\n\n'+' · '.join(f'[{label}]({prefix}docs/{lang}/{page})' for lang,label in zip(docs.LANGUAGES,('简体中文','English','日本語')))+'\n\nAIChat 1.18.30 + SPP 5.10.10 · 2026-10-08\n').encode()

def document_payload():
    docs.ROOT = ROOT
    docs.MANIFEST = MANIFEST.relative_to(ROOT).as_posix()
    docs.REVISION = 'BUILD_INFO.json'
    docs.gateway = gateway
    result = docs.document_payload()
    for component in ('AIChat', 'SatonePromptProxy'):
        for lang in docs.LANGUAGES:
            name=f'{component}/docs/{lang}/DOWNLOADS.md'
            result[name]=result[name].replace(b'../../BUILD_INFO.json', ('https://github.com/Scaleph-Enkidu/SatonePromptProxy-SPP-_Releases/blob/main/releases/'+NAME+'.json').encode())
    # A generic checklist replaces the former release-specific entry in this new ZIP.
    result['01_验证清单.md'] = result.pop('01_N15实机验证清单.md')
    return result

def build(ai_bin, spp_exe):
    assert sha(BASE.read_bytes()) == BASE_HASH
    with zipfile.ZipFile(BASE) as z:
        original = {n: z.read(n) for n in z.namelist()}
    payload = {n: b for n,b in original.items() if n != 'BUILD_INFO.json' and (not n.endswith('.md') or '/third_party/' in n)}
    payload.update(document_payload())
    replacements = {'AIChat/AIChat.dll': ai_bin/'AIChat.dll', 'AIChat/AIChat.pdb': ai_bin/'AIChat.pdb', 'SatonePromptProxy/SatonePromptProxy.exe': spp_exe}
    for name,p in replacements.items():
        data=p.read_bytes()
        assert sha(data)==BINARIES[name], f'Unexpected binary: {name}'
        payload[name]=data
    preserved = {n:sha(b) for n,b in original.items() if n in payload and payload[n]==b}
    info = {'schema_version':3, 'release_tag':TAG, 'generated_on':'2026-10-08', 'versions':VERSIONS,
            'source_commits':SOURCES, 'runtime_tested_commits':TESTED, 'languages':list(docs.LANGUAGES),
            'build_provenance':{'AIChat':'net472 Release build from source_commits.AIChat; matching DLL/PDB rebuilt for this release; differs from the earlier sealed DLL. Production source unchanged from runtime_tested_commits.AIChat.',
                                'SPP':'Exact Windows EXE from the sealed RR round-1 test run at runtime_tested_commits.SPP; production source unchanged at source_commits.SPP.'},
            'prior_validation':{'go_pass':666,'go_skip':9,'exe_pairs_pass':5,'csharp_assertions':1548},
            'release_validation':{'date':'2026-10-08','net472_release_build':'0 warnings, 0 errors',
                                  'csharp_projects_pass':7,'csharp_assertions_pass':1548,
                                  'extracted_spp':'first start and restart with empty PATH; health reports 5.10.10; persona, recall/status and asr/status HTTP 200',
                                  'source_identity':'Both remote main commits match source_commits; production code unchanged from runtime_tested_commits.'},
            'validation_limits':['No new real-game, microphone, live-provider or external-model acceptance run.','Historical N15 field-test results apply only to that old release.'],
            'binaries_sha256':BINARIES, 'original_package_sha256':BASE_HASH,
            'preserved_original_members_sha256':preserved,
            'files_sha256':{n:sha(b) for n,b in sorted(payload.items())}}
    payload['BUILD_INFO.json']=jb(info)
    PACKAGE.mkdir(parents=True,exist_ok=True)
    target=PACKAGE/ZIP
    with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for n,b in sorted(payload.items()):
            zi=zipfile.ZipInfo(n,(2026,10,8,0,0,0)); zi.compress_type=zipfile.ZIP_DEFLATED; zi.external_attr=0o100644<<16
            z.writestr(zi,b,compresslevel=9)
    checksum=sha(target.read_bytes())
    (PACKAGE/(ZIP+'.sha256')).write_text(f'{checksum}  {ZIP}\n',encoding='ascii',newline='\n')
    manifest=dict(info,package_directory=PACKAGE.relative_to(ROOT).as_posix(),package_file=ZIP,package_sha256=checksum,package_bytes=target.stat().st_size,
                  zip_members_sha256={n:sha(b) for n,b in sorted(payload.items())})
    MANIFEST.write_bytes(jb(manifest))
    print(json.dumps({'zip':str(target),'bytes':target.stat().st_size,'sha256':checksum,'members':len(payload)}))

def verify(directory=None):
    m=json.loads(MANIFEST.read_bytes())
    directory=directory or PACKAGE
    target=directory/ZIP
    assert m['release_tag']==TAG and m['versions']==VERSIONS and m['source_commits']==SOURCES
    assert target.stat().st_size==m['package_bytes'] and sha(target.read_bytes())==m['package_sha256']
    assert (directory/(ZIP+'.sha256')).read_text().split()==[m['package_sha256'],ZIP]
    with zipfile.ZipFile(target) as z:
        check_archive(z,list(m['zip_members_sha256']))
        packed={n:z.read(n) for n in z.namelist()}
    for n,b in packed.items(): assert sha(b)==m['zip_members_sha256'][n],n
    info=json.loads(packed['BUILD_INFO.json'])
    assert info['versions']==VERSIONS and info['source_commits']==SOURCES
    assert set(packed)==set(info['files_sha256'])|{'BUILD_INFO.json'}
    for n,h in info['files_sha256'].items(): assert sha(packed[n])==h,n
    for n,h in BINARIES.items(): assert sha(packed[n])==h,n
    assert not any(n.endswith('.onnx') or n.endswith('DOCUMENTATION_REVISION.json') for n in packed)
    assert sha(BASE.read_bytes())==BASE_HASH
    with zipfile.ZipFile(BASE) as z:
        for n,h in info['preserved_original_members_sha256'].items(): assert sha(z.read(n))==sha(packed[n])==h,n
    # The only changed runtime payloads are the two components' versioned binaries.
        oldruntime={n:z.read(n) for n in z.namelist() if not n.endswith('.md') and n!='BUILD_INFO.json'}
        for n,b in oldruntime.items():
            if n not in BINARIES: assert packed[n]==b, 'Unexpected auxiliary payload change: '+n
    errors=[]
    for prefix in ('','AIChat/','SatonePromptProxy/'):
        files={n[len(prefix):]:b for n,b in packed.items() if n.startswith(prefix)}
        scope=[n for n in files if n=='README.md' or n.startswith(tuple('docs/'+l+'/' for l in docs.LANGUAGES)) and n.endswith('.md')]
        errors += docs.check_links(files,set(files),scope)
        assert all(label.encode() in files['README.md'] for label in ('简体中文','English','日本語'))
        pages=[{n[len('docs/'+l+'/'):] for n in files if n.startswith('docs/'+l+'/') and n.endswith('.md')} for l in docs.LANGUAGES]
        assert pages[0]==pages[1]==pages[2]
    repo_files={p.relative_to(ROOT).as_posix():p.read_bytes() for p in (ROOT/'docs').rglob('*.md')}
    repo_files['README.md']=(ROOT/'README.md').read_bytes()
    names={p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if '.git' not in p.parts}
    scope=[n for n in repo_files if n=='README.md' or n.startswith(tuple('docs/'+l+'/' for l in docs.LANGUAGES))]
    errors += docs.check_links(repo_files,names,scope)
    for n,b in document_payload().items(): assert packed[n]==b,'Stale packaged guide: '+n
    assert not errors, '\n'.join(errors)
    if directory != PACKAGE:
        assert {p.name for p in directory.iterdir()}=={ZIP,ZIP+'.sha256',MANIFEST.name}
        assert (directory/MANIFEST.name).read_bytes()==MANIFEST.read_bytes()
    print(f'PASS: ZIP, binaries, all {len(packed)} members, licenses/auxiliary preservation, trilingual and standalone offline links.')

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ai-bin',type=Path)
    parser.add_argument('--spp-exe',type=Path)
    parser.add_argument('--verify',action='store_true')
    parser.add_argument('--assets-dir',type=Path)
    args=parser.parse_args()
    if not args.verify:
        assert args.ai_bin and args.spp_exe
        build(args.ai_bin,args.spp_exe)
    verify(args.assets_dir)
