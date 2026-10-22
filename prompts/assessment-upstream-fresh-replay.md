# Fresh Control Plane handoff — independent assessment-to-upstream test

Copy the following request into a **new ChatGPT conversation** with the OpenSiro OSS Control Plane. This prompt deliberately names **no past harness, issue or PR**. The control documents point to the bounded public ecosystem; historical case outcomes must not be consulted before first selection. It is a prompt, not an automation, delegated decision right, permission grant or guarantee of an independent runtime.

---

Проведи **новый независимый тест** `test S1 function: upstream contributions` в режиме `FRESH_INDEX_FIRST`.

1. Начни с текущего публичного [START_HERE](https://github.com/opensiro/vsm-oss-organization/blob/main/START_HERE.md), затем `docs/ECOSYSTEM.md`, `docs/AGENT_CONTROL_PLANE.md` и `docs/ASSESSMENT_UPSTREAM_REPLAY.md`. Следуй текущим источникам, а не памяти этого чата.
2. **Не используй прошлые переписки, готовые списки кандидатов, пилотные PR, старые кейсы и подсказки о результате**. До первого зафиксированного выбора не открывай историю `opensiro/upstream` #56, прошлые `pilots/`, `candidates/`, `docs/reviews/` или issues выбранного внешнего harness. Если уже знаешь о предыдущем кандидате из памяти, явно отметь `POTENTIALLY_CONTAMINATED` и не заявляй независимый first attempt.
3. **Сначала самостоятельно выбери assessment из текущего канонического Index** и конкретный наблюдаемый недостаток функции/владения решением/обратной связи. Зафиксируй SHA Index, путь assessment, `review_ref`, функцию, доказательство, гипотезу, возможный отрицательный результат и порядок выбора **до** изучения issue внешнего проекта.
4. После фиксации выбора проверь актуальный upstream: код, default branch, потребность продукта, существующие PR/issue, contribution rules и четыре независимых gate `need/mechanism/counterfactual_value/scope`.
5. Если проверки позволяют, подготовь воспроизводимый реальный baseline и **сопоставимый** after на конкретном поведении harness. Не выдавай synthetic planner/output-only тест за доказанное предотвращение проблем реальных агентов; не меняй VSM-оценку ради улучшения метрики.
6. Самостоятельно выполняй допустимые read-only проверки и уже разрешённые локальные/внутренние действия. Внешние issue, fork, push, публикация PR или merge требуют текущих прав и правил исходного проекта. Режим теста сам по себе не выдаёт разрешений, а `продолжай` не заменяет точную авторизацию.
7. В конце выдай сравнение со старой практикой **только после selection lock**: provenance, baseline, after, эффект, неопределённости, status внешнего PR/merge и фактические решения Control Plane. Другой кандидат, `NO_ELIGIBLE_ASSESSMENT_CANDIDATE` или честный `BLOCKED_EVIDENCE` — валидный исход.

Цель — **повторить корректную причинно-следственную процедуру**, а не угадать систему из прошлого эксперимента. Не останавливайся из-за мелких вопросов; исполняй все допустимые действия до реального технического или authority-блокера. Не заявляй работу в фоне.

---

**Control Plane's machine check:** [Organization CI](https://github.com/opensiro/vsm-oss-organization/actions/workflows/contract-consistency.yml) validates **static documentation conformance only**. A genuinely fresh conversation must still produce a visible first-attempt selection receipt and independently validated native evidence.
