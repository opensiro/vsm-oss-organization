# W002 S3* semantic finding — Index #1006 row 1 SuisuiCode, unreachable default S4 updater

**Audit ID:** `S3STAR-INDEX-BATCH-20261011-W002-1006-R01-S4-001`  
**Exactly one local audit outcome: `FINDING`** on the accepted positive `S4=A` boundary/reachability premise. The observed source defect does **not** authorize a categorical replacement grade, an Index reassessment commit, or new S1 lock; the owning Index issue must adjudicate the finding against the same frozen ref. The frozen whole-batch #1006 state remains **`INSUFFICIENT/PENDING`** (only 2/10 original rows terminal, preregistered positions 5/10 unavailable).

## Audit identity, ordinary reporting, and control scope

- **System-in-focus:** first-party Organization S3* complementary audit of public Index S1 assessment assertions, **not** the upstream harness's own `autonomy_s3_star`. W002 governed by [Organization #190](https://github.com/opensiro/vsm-oss-organization/issues/190), sample #1006 position 1, immutable Index intake #878; not W001's frozen ten batches.
- **Audited code:** [Yangtianspike/suisui-code@`c9017b0613b22151325a5904a521aefe4c62abbc`](https://github.com/Yangtianspike/suisui-code/tree/c9017b0613b22151325a5904a521aefe4c62abbc), full 321-entry untruncated Git tree. **Accepted S1 artifact:** [Index `assessments/suisuicode.md` at frozen Index main](https://github.com/opensiro/vsm-harness-index/blob/0db4a2ecdefe9c2641306ab20fc17eab114e0681/assessments/suisuicode.md), included catalog #344, vector `A · C · A · — · A · —`, generated Profile 0.2.4 / Skills Methodology 0.3.6.
- **Claim under challenge:** its S4 section states automatic long-term model-owned guidance adaptation: CLI creates the memory manager, a completed Agent turn calls `memory.Manager.update_async`, the updater uses an LLM to choose future-oriented `create/update/delete` changes, the Store persists them, and later CLI sessions load the result. Crucial explicit qualifier: **"when a provider is configured."** This is a reachability claim about the **standard shipped composition**, not mere existence of a callable model updater.
- **Routine S1 evidence path:** published assessment interpretation, user-facing feature names, generated Index signature, structural Index validation and historical merged review/admission PRs. None proves the provider is actually installed in the separate memory updater object.

## Materially complementary exact-source data-flow trace

1. [`src/suisuicode/cli.py#L139-L151`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/cli.py#L139-L151) constructs the only standard CLI memory manager explicitly as `Manager(project_dir=..., user_dir=..., provider=None, model="")`, with a comment saying provider will be assigned later, then immediately calls `memory_text = mem_mgr.load_index()` (this read-path is real).
2. [`src/suisuicode/cli.py#L307-L325`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/cli.py#L307-L325) passes `mem_mgr` and a frozen `memory_text` snapshot into the `new_app` factory, not the actual selected model provider. Independently inspected the complete pinned `cli.py` (385 lines): no later call to `mem_mgr.set_provider`, `_provider` assignment or replacement of that memory Manager is present.
3. [`src/suisuicode/tui/app.py#L702-L731`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/tui/app.py#L702-L731) creates `self._provider_instance = new_provider(provider)` upon provider selection and invokes `self._ensure_agent()`. [`_ensure_agent` at lines 770–788](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/tui/app.py#L770-L788) passes that provider **to the main Agent** and separately injects `memory_manager=self._mem_mgr`, but **never calls `self._mem_mgr.set_provider(self._provider_instance, ...)`**. Reviewed complete `app.py` (1765 lines): `_mem_mgr` is retained, handed to Agent, or queried for file listing; **there is no updater-provider binding at any provider selection or subsequent lifecycle step**.
4. [`src/suisuicode/agent/agent.py#L545-L569`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/agent/agent.py#L545-L569) genuinely creates an async `self._mem_mgr.update_async(recent_msgs)` task after a completed main Agent turn. This call does not itself supply a Provider.
5. [`src/suisuicode/memory/manager.py#L116-L142`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/memory/manager.py#L116-L142) offers an explicit `set_provider(provider, model)` setter (which **could** enable the feature for an external caller), but its `update_async` returns immediately when `self._provider is None`. [`_do_update` lines 144–212](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/memory/manager.py#L144-L212) contains the model invocation and action selection, **unreachable via that normal CLI/TUI initialization path** without a missing provider-binding step.
6. [`src/suisuicode/memory/prompts.py#L1-L79`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/memory/prompts.py#L1-L79) defines real user-correction/project-adaptation instructions (including `Why` and `How to apply`), and Store supports create/update/delete. These establish an **implemented but inert as shipped** conditional capability, not a completed **boundary-reachable default autonomous S4 loop**. An operator or another integration could explicitly invoke `set_provider`; this record makes **no universal assertion** that all hypothetical compositions are unable to use it.
7. The accepted `S3=A` path is distinct: [`cli.py#L116-L131`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/cli.py#L116-L131) registers TaskList/Get/Stop/SendMessage; [`task/manager.py#L112-L210`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/task/manager.py#L112-L210) tracks background Agent lifecycle; [`task/tools.py#L115-L213`](https://github.com/Yangtianspike/suisui-code/blob/c9017b0613b22151325a5904a521aefe4c62abbc/src/suisuicode/task/tools.py#L115-L213) exposes real cancel/re-task. This audit **does not find a contradiction** to autonomous S3 through that separate current-control path. Earlier Team-mode architecture caveats remain as historically reported, not treated as source of S3/S4 positives.

## Exact S3* judgment

- **`FINDING`:** the **main-agent provider is not wired to the memory manager's provider field** in the shipped CLI + TUI startup path at the exact frozen SHA; thus the only stated automatic memory-model adaptation path silently returns before requesting the LLM. Merely loading existing `MEMORY.md` cannot recover the claimed model-owned *new* prospective adaptation. The accepted `S4=A` relies on a first-party **boundary reachability assertion contradicted by observed initialization and guard code**.
- **Disposition demanded, not preselected:** original Index owner should independently assess whether the correct same-ref S4 state would be `?`, `—`, or otherwise conditional under Profile 0.2.4 / methodology 0.3.6, or identify a source-grounded alternative reachable S4 closure. This S3* auditor does **not** arbitrarily assign `—`: negative absence requires the original methodology's complete search scope.
- **Verification limitations:** static pinned-source data-flow, not a real provider-backed end-to-end run. Confidence high that the documented default CLI path leaves `Manager._provider=None`, subject to unforeseen external monkey-patching or a separately constructed app which is not claimed here. `test_memory.py` covers `no_provider` safe return, Store CRUD, and index loading, not a standard CLI→new_provider→memory update end-to-end success.
- **Complementarity and attribution:** the W002 ChatGPT auditor exercises discretionary source-vs-claim judgment by tracing two separately constructed provider-bearing objects; GitHub connector, static search and Index CI remain evidence machinery, not audit decision owners. Historical producer's GitHub account may overlap the present connected account, and no new external or formal independent GitHub review is claimed.

## Downstream control / owner / closure

**Exact owning destination:** [Index #1006](https://github.com/opensiro/vsm-harness-index/issues/1006), already-admitted row 1 SuisuiCode at same frozen SHA, catalog #344, original review PR #1066 and admission PR #1067. Request **independent source-citable adjudication and a reviewable same-ref correction if the source finding survives**. Do not directly edit the canonical row, alter signatures, advance row 3 WhipCode `NEXT`, audit rows5/10 before terminalization, repin to newer source, or cross into W001.

**Local `FINDING` remains OPEN until actual Index decision and any correctly gated correction can be verified on live main.** Publication of this record or notification to Index is **not** S3 exceptional-current-control closure and **not** proof of an autonomous Organization S3* state.

**Batch result retained:** #1006 `INSUFFICIENT/PENDING`; five previously accepted bounded PASS batch outcomes elsewhere in W002 are unaffected, as are 35 other nonterminal row slots.

## Local frozen-source executable reproduction (separate from static path proof)

An **isolated** workspace was created solely for *read-only upstream probing*, not Index canonical mutation. Git initialized and fetched the exact original upstream commit as a detached shallow checkout; independently observed `git rev-parse HEAD == c9017b0613b22151325a5904a521aefe4c62abbc`; `git status --short` empty. A whole-repository tracked-Python search:

```sh
git grep -n -E 'set_provider\(|_mem_mgr\._provider|mem_mgr\._provider' -- '*.py'
```

returned **exactly** `src/suisuicode/memory/manager.py:117: def set_provider(...)` and no call site in tracked Python sources. This broadens the main CLI/TUI inspection to all pinned tracked Python files; it is still not a formal control-flow or test of every dynamic/plugin entrypoint.

Executed the **real frozen** `suisuicode.memory.manager.Manager` implementation with `PYTHONPATH=src`, an isolated tempfile as project/user Store, a lightweight deterministic test provider that returns a valid `create` action, and a single synthetic user message. The following probe deliberately compares the **same Manager** before and after an explicit setter:

```python
import asyncio, pathlib, tempfile, types
from suisuicode.memory.manager import Manager

class ProbeProvider:
    def __init__(self):
        self.calls = 0

    async def stream(self, request):
        self.calls += 1
        action = '[{"action":"create","level":"project","name":"future-rule",' \
                 '"description":"Future rule","type":"feedback",' \
                 '"content":"remember this"}]'
        yield types.SimpleNamespace(text=action, err=None, done=True)

async def check():
    with tempfile.TemporaryDirectory() as tmp:
        root = pathlib.Path(tmp)
        provider = ProbeProvider()
        mgr = Manager(str(root / "project"), str(root / "user"), provider=None)
        recent = [types.SimpleNamespace(role="user", content="Remember this")]
        await mgr.update_async(recent)
        assert mgr._provider is None
        assert provider.calls == 0
        assert not (root / "project" / "future-rule.md").exists()

        mgr.set_provider(provider, "probe")
        await mgr.update_async(recent)
        assert provider.calls == 1
        assert (root / "project" / "future-rule.md").exists()

asyncio.run(check())
```

The exact Python snippet below (also re-extracted directly from this committed Markdown code fence) was independently executed in the same exact-commit checkout with `PYTHONPATH=src` and exited **0**, printing `DOCUMENTED_REPRO_EXIT_0`. It uses an in-process deterministic provider, not external API/model credentials.

**Actual run result (exit 0, diagnostic variant with prints):**

```text
WITHOUT_BINDING: provider_is_none= True provider_calls= 0 notes= 1
WITH_EXPLICIT_BINDING: provider_calls= 1 created_note= True
```

The one note counted before binding is the **empty `MEMORY.md` index created during Store initialization**, **not** a learned or updated future-rule memory; the explicit target note is absent before binding and present afterwards. This proves the pinned updater's provider-null guard prevents even a stub LLM call and that explicit binding changes the behavior. It does **not** execute the whole CLI/TUI live session, establish a real provider-backed learning quality, or choose a replacement VSM grade. Attempt to run focused `tests/test_memory.py` with `python3 -m pytest` was **NOT RUN** because `pytest` is not installed in this isolated environment (`No module named pytest`), not claimed as a test success/failure in the upstream harness. No upstream files were changed.

**S3* impact:** strengthens the original source-native `FINDING` and its confidence; no change to cohort, sampling, published Index grade, W002 batch-level `INSUFFICIENT/PENDING` or Index correction authority. The owner can reproduce using the immutable upstream SHA.
