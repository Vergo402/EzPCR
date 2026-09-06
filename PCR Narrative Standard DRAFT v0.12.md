# PCR Narrative Standard, Draft v0.12
Cortlandt-Peekskill Regional Paramedic Services, emsCharts, NYS ALS Collaborative Protocols
Author: A. Vergo. Status: working draft, aligned to NYS Collaborative Protocols v26.1 (eff. 9/1/26) and the National Field Triage Red/Yellow criteria. Shell, four dispositions, all 18 blocks, all 6 dedicated templates. Complete first full draft.

Conventions
- `___` = fill in. `[ ]` = pick one or delete. `{ }` = note to self, delete before saving.
- A bracket followed by `{any that apply}` means the options combine (any subset), joined in prose as an Oxford list ("a and b" / "a, b, and c").
- Routine data lives in the emsCharts activity log. The narrative restates only values that justify a decision.
- Protocol names stay out. Cite only medical control contact and any deviation.
- Every block ends with its escalation line. If it fires, stop the block and switch to the dedicated template.
- Withheld treatments are written next to the drug they belong to, with the reason.
- GCS appears only in the Neuro/AMS and Trauma blocks.
- The finished narrative is a fixed shell of four paragraphs with the stacked material printed between the third and the fourth: (1) initial — dispatch, primary, mental status/CC/history; (2) vitals; (3) assessment — impression, secondary/exam; then **each block or template as its own paragraph, in the order they were stacked**; then (4) disposition — ongoing/transport and disposition. Sentences and whole blocks may still be rearranged, including into a different paragraph, to match the order things actually happened; the shell paragraphs and the block-per-paragraph rule are the frame.
- A sentence that two stacked blocks both carry (analgesia withheld, 12-lead, IV access, GCS after an escalation) is written once. The first block in the chart states it; the builder hides the later block's copy unless the medic shows it. The twin groups are listed in the builder's DOC meta.
- Scored fields (GCS, NYS-LAMS, burn % BSA) are entered as their components; the builder computes the total. In the sentence the total keeps the position the standard prints.

---

## 1. SHELL (every call)

**Dispatch / Response / Arrival**
35M___ dispatched to ___ for ___. 35M___ responded [emergency / non-emergency]. 35M___ arrived on scene (___ on location) and found ___ yo [M / F / other…] pt ___ {position, location, appearance, scene}.

**Primary**
{traumaGeneral / traumaMinor / burns only — traumaMajor uses its own spinal motion restriction line in §6:} Spinal motion restriction: [c-collar applied and secured to stretcher for ___ {AMS or intoxication, neck/spine pain or tenderness, weakness/tingling/numbness since injury, spinal deformity, distracting injury, high-risk MOI: axial load, high-speed MVC/rollover, ped or bike struck, fall >3 ft/5 steps/pt height, or Red criteria blunt} / not indicated: no AMS, no spine pain or tenderness, no neuro sx, no deformity, no distracting injury, MOI not high-risk {use caution >65}].
Pt [+ / - / other…] patent airway, [+/-] breathing w/ initial L/S [bilateral / clear / other…], [+ / - / Reg / IRR / IR / Radial / Carotid / Femoral / other…] {any that apply} ___ pulse {location, quality}, skin ___.
{Conditional line, only if something was done before the full assessment:} ___ {e.g. "Pt placed on NRB 15 LPM." "Narcan 4 mg IN administered." "Tourniquet applied R thigh ___." Delete if nothing.}

**Mental status / CC / History**
Pt A&Ox___ (P, P, T, E), [A/V/P/U], [+ LOC ~___ min / - LOC / unknown LOC], and complaining of ___ {onset, duration, in pt's words}. [Pt / bystanders / family / healthcare staff / other…] state ___.
Pt PMHx ___. Meds [per list / noncompliant ___ / other…] {any that apply}. Allergies [NKDA / ___]. {Add: last oral intake, DNR/MOLST status when relevant.}

**Assessment**
Vitals as noted in emsCharts activity log, [stable / concerning for ___] {restate only the numbers that drive the DDx or a treatment}.
Working impression ___. DDx ___.

**[BLOCK SLOT]**
{Where the call-type blocks and templates are authored — treatments, withheld treatments with reason, reassessment, escalation line. This marks authoring position, not print position: each stacked block or template prints as its own paragraph AFTER the assessment paragraph (impression, then Secondary below) and before the disposition paragraph, in the order they were stacked.}

**Secondary**
Secondary assessment [focused ___ / head-to-toe exam] unremarkable except ___.

**Ongoing / Medical control**
Pt reassessed en route: ___ {the load-bearing change: pain 7 to 3, SpO2 88 to 96, rhythm unchanged}. Remaining vitals per activity log.
{Delete if none:} Medical control contacted, Dr. ___ at ___, orders received for ___. {Any protocol deviation named here, plainly.}

**Disposition (pick one)**

*1) ALS transport*
Pt txp ALS to ___. Hospital notified via [cell / radio / smartphone app / other…]. [No pt changes throughout txp / other…]. Pt transferred to ED staff, report given to RN. 35M___ returned to service without further incident.

*2) Transport BLS*
Pt assessed, no ALS intervention indicated: ___ {the reason in one clause: 12-lead no acute changes, vitals stable, BGL normal, pain controlled}. Pt released to ___ {agency} BLS crew for txp to ___, report given to EMT. Pt [stable / unchanged] at time of release. 35M___ returned to service without further incident.

*3) 35M# cancelled*
35M___ cancelled [en route / on scene / other…] by ___ {agency, unit, or dispatch} for ___ {e.g. no pt found, pt refused prior to arrival, or BLS handling}. [No pt contact made. / other…] 35M___ returned to service without further incident.

*4) RMA by 35M#*
Pt [refuses transport / refuses assessment / other…] against medical advice. Pt A&Ox4, [no evidence of AMS, intoxication, head injury, suicidal intent, or irrational behavior / other…], demonstrates capacity by restating in own words the nature of the complaint and the consequences of refusing. Transport to hospital offered. Pt advised that refusing may increase the possibility of serious illness, permanent disability, and death, including ___ {the worst plausible outcome for this complaint}. Pt advised to seek medical attention, follow-up instructions given: ___. Pt confirmed understanding and continues to refuse. Pt advised to call 911 with any return or worsening of symptoms. High-risk refusal [N / Y: ___ {age >65, HR >120 or <50, SBP >200 or <90, RR >29 or <10, CP/SOB/syncope/focal deficit, significant MOI, ALS meds given}, medical control contacted, see above]. RMA signed by pt, witnessed by ___ {PD, family, partner}. Pt left in care of [self / responsible adult ___ / other…]. 35M___ returned to service without further incident.

---

## 2. CARDIAC BLOCK
Categories: Cardiac Related Problem, Chest Pain, Heart Problems, Hypertension (symptomatic), Hypotension
Two sub-blocks. Chest pain with a normal rhythm uses 2a only. A rhythm problem without chest pain uses 2b only. Both when both.
Escalates to: STEMI template (2a). Cardiac Arrest template if pulses lost (2b). Hypotension with a shock picture: name the etiology in DDx and add the matching block (Tox, Sepsis, Trauma, Allergic).

### 2a. Cardiac / ACS
Pt describes ___ {OPQRST}. Associated [none / SOB / diaphoresis / N/V / lightheadedness / syncope / palpitations / other…] {any that apply}. Cardiac risk factors [diabetes mellitus / FHx / HTN / hyperlipidemia / prior MI/CABG/stent / smoker / stimulant use / other…] {any that apply}.
12-lead acquired: ___ {rhythm, rate, axis, intervals, ST/T changes by lead, or "no acute changes"}, transmitted. {If inferior changes: R-sided 12-lead ___. If STE: jump to escalation line.}
ASA 324 mg chewed [administered / withheld: ___ {allergy, unable to chew, active GI bleed}]. {Took ASA before arrival but dose uncertain: give and say why.}
NTG 0.4 mg SL [x___, ___ min apart, SBP ___ before each dose, pain ___ to ___/10 / withheld: ___ {SBP ≤120 or MAP ≤90, R-sided changes, phosphodiesterase-5 inhibitor within 48h}]. {SBP drops <100 after NTG: supine, NS 500 mL bolus, reassessed ___.}
IV ___g ___.
Fentanyl ___ mcg [IV / IM / IN] for pain ___/10 unrelieved by NTG, pain ___ to ___/10 / withheld: ___ {pain improved, pt declined, SBP, AMS}. {No ketorolac in suspected ACS.}
{Symptomatic HTN only:} BP ___ with ___ {headache, vision change, CP, neuro deficit}. Neuro exam ___. No antihypertensive given.
{Hypotension only:} SBP ___, ___ {skin, mental status, cap refill}. ___ mL NS bolus, reassessed SBP ___. {Pressor only w/ med control, cite in Medical control line.}
{If performed:} Serial 12-lead: [unchanged / other…].
**Escalation line:** STEMI criteria [not met on serial 12-leads / MET: ___ {leads, mm}, STEMI alert called to ___, 12-lead transmitted. Switch to STEMI template.]

### 2b. Cardiac / Dysrhythmia
Monitor: ___ {rhythm, rate, regularity, QRS width, P-wave relationship, block degree and type}. 12-lead confirms ___. {Print and attach the strip that shows the diagnosis.}
Pt [hemodynamically stable / UNSTABLE: ___ {which of: SBP <90, AMS, ischemic CP, acute CHF, syncope}]. Onset ___ {known time, or "unknown, >48h" for rate-control decisions}. Prior Hx of this rhythm [Y, ___ / N]. Anticoagulated [Y ___ / N].
IV ___g ___.
{If performed:} Pads applied [prophylactically / for pacing / for cardioversion].

{Pick the fork that applies. Delete the rest.}

*Bradycardia:*
Atropine 1 mg IV, x___, HR ___ to ___, [symptoms resolved / no response] / withheld: ___ {asymptomatic, 2nd-degree type II or 3rd-degree block with poor perfusion went straight to pacing, transplant}.
TCP initiated, rate ___, capture at ___ mA confirmed by [palpable pulse / SpO2 pleth / other…]. Sedation: midazolam [2.5 mg IV / 5 mg IM] / withheld: ___ {SBP, AMS}.
Epi infusion started at ___ mcg/min, titrated to ___ mcg/min, MAP ___ to ___ / not indicated: ___.

*Narrow-complex tachycardia:*
{Stable, REGULAR:} Vagal maneuver [modified Valsalva / other…], [converted / no change]. Adenosine 6 mg rapid IV with flush, [converted to ___ / no change / transient block revealing ___]. Adenosine 12 mg, ___.
{Stable, IRREGULAR:} [Diltiazem ___ mg IV over 2 min {0.25 mg/kg, max 25 mg} for ___ {A-fib/flutter RVR}, HR ___ to ___, BP ___ to ___ / metoprolol 5 mg IV over 2 min (pt on Rx beta-blocker)] {any that apply} / withheld: ___ {SBP, WPW, CHF}. {Uncontrolled after 15 min or recurrent:} Diltiazem ___ mg {0.35 mg/kg, max 35 mg} / second metoprolol 5 mg.
{UNSTABLE, regular or irregular:} Sedation [midazolam 2.5 mg IV / 5 mg IM] ___ / withheld: ___ {SBP, AMS, time-critical}. Synchronized cardioversion 200 J, [converted to ___ / repeated at ___ J]. Pt [aware / not aware] during shock. 12-lead post-conversion: ___.

*Wide-complex tachycardia:*
QRS ___ ms. Treated as VT [stable / UNSTABLE].
{Stable:} [Amiodarone 150 mg in 100 mL NS over 10 min / lidocaine IV / other…] {any that apply}, [converted / no change / other…] / withheld: ___ {unstable, went to cardioversion; polymorphic}.
{UNSTABLE:} Sedation [midazolam 2.5 mg IV / 5 mg IM / other…] / withheld: ___. Synchronized cardioversion 100 J {200 J if irregularly irregular; max 3 attempts}, [converted to ___ / repeated ___ J, ___ J / other…]. Antiarrhythmic post-conversion per med control: ___.
{Torsades / med control:} Mag 2 g IV over [10 min stable / 2 min unstable] per Dr. ___.

Post-intervention rhythm ___, 12-lead: ___. Pt [symptoms resolved / other…].
**Escalation line:** Pt remained [hemodynamically stable / stable after intervention / Unstable] throughout / became unstable, ___ {intervention} / other…. Pulses [maintained throughout / LOST. Switch to Cardiac Arrest template.]

---

## 3. RESPIRATORY BLOCK
Categories: Breathing Problems, Choking, COVID-19 Related/Potential
Escalates to: Respiratory Arrest template. Allergic block if anaphylaxis is the cause. Cardiac block if CHF from a rhythm or ACS.

Pt [speaking full sentences / ___-word sentences / unable to speak], [tripod / supine / ___], accessory muscle use [Y / N], [retractions / nasal flaring / pursed lips / none] {any that apply}. RR ___, SpO2 ___% on [RA / ___]. L/S ___ {by field: clear, wheezes, rales, rhonchi, diminished, absent}, ETCO2 ___ with [normal / shark-fin / ___] waveform.
Onset ___ {sudden / gradual over ___}, [exertional / at rest], associated [fever / productive cough ___ / CP / orthopnea / paroxysmal nocturnal dyspnea / leg swelling / recent illness / sick contacts / travel / none]. Hx [asthma / COPD / CHF / PE / smoker ___ packs per day / home O2 ___ LPM / prior intubation for this]. Rescue inhaler used ___ times prior to arrival.
Working etiology ___ {reactive airway, CHF/pulmonary edema, pneumonia, PE, pneumothorax, FBAO, other}.

O2 via [NC / NRB / BVM] ___ LPM, SpO2 ___ to ___.
{Pick the fork that applies. Delete the rest.}

*Reactive airway (asthma / COPD):*
Albuterol 2.5 mg / ipratropium 0.5 mg neb, repeated, ___ {max 3 albuterol on standing order}, L/S ___ to ___, RR ___ to ___ / withheld: ___.
Dexamethasone 10 mg [IV / IM / PO] / withheld: ___.
Mag 2 g in 100 mL NS IV over 10 min for asthma not responding to above / withheld: ___. {COPD: med control only, cite.}
Epi 0.3 mg (1 mg/mL) IM for severe distress / withheld: ___.
CPAP ___ cmH2O {5-10}, tolerated [well / ___], SpO2 ___ to ___ / withheld: ___ {AMS, vomiting, SBP, unable to protect airway}.

*CHF / pulmonary edema:*
CPAP ___ cmH2O {5-10}, tolerated [well / ___], SpO2 ___ to ___, RR ___ to ___ / withheld: ___ {SBP, AMS, vomiting, facial trauma}.
NTG 0.4 mg SL [x1 / x2 / x3] per SBP ___ {SBP 120-160: 1 tab q5; 160-200: 2 tabs q5; >200: 3 tabs q5}, BP ___ to ___ / withheld: ___ {SBP <120, phosphodiesterase-5 inhibitor}.
12-lead: ___ {rhythm, ischemic changes}. {If ACS suspected, add 2a.}

*FBAO (Choking):*
[Partial / complete] obstruction, pt [coughing effectively / unable to cough or speak / unresponsive] on arrival. Abdominal thrusts x___ by [bystander / crew]. Laryngoscopy, ___ {object seen or not}, removed with Magill forceps / not visualized. Airway [patent after removal / ___]. Post-event L/S ___, SpO2 ___.

*Pneumonia / infectious / COVID:*
Temp ___, [sepsis screen: see Metabolic/Sepsis block if positive]. Isolation precautions ___. Supportive O2 as above.

*Suspected pneumothorax:*
L/S [absent / diminished] ___ side, [tracheal deviation / JVD / subcutaneous emphysema / none]. {Tension with hemodynamic compromise:} Needle decompression ___ side, ___ ICS ___ line, [rush of air / improvement in ___] / not indicated: ___.

Pt reassessed: [work of breathing improved / unchanged / worsening], RR ___, SpO2 ___, ETCO2 ___, L/S ___.
**Escalation line:** Pt [maintained adequate spontaneous respirations throughout / respirations became inadequate, BVM initiated. Switch to Respiratory Arrest template.]

---

## 4. NEURO / AMS BLOCK
Categories: Altered Mental Status, Dizziness, Headache, Seizure, Syncope (near), Syncope/Fainting, Unconscious/Unresponsive
Escalates to: Stroke/CVA template. Tox block if overdose is the cause. Metabolic block if hypoglycemia or sepsis is the cause and corrected. OB block for seizure in pregnancy or ≤6 wks postpartum.

GCS ___ (E___ V___ M___), pupils ___ {size, equality, reactivity}. Baseline mental status per [family / facility / ___]: ___. Last known well ___ {time and source}.
BGL ___. Temp ___. {SpO2 and ETCO2 per activity log unless abnormal: ___.}
NYS-LAMS: facial droop [absent 0 / present 1], arm drift [absent 0 / drifts 1 / falls rapidly 2], speech [normal 0 / abnormal 1], grip [normal 0 / weak 1 / none 2], total ___/6. [Negative, no deficits / POSITIVE ___, see escalation line].
Onset ___ {sudden / gradual}, [witnessed by ___ / unwitnessed, found at ___]. Associated ___ {headache, worst-ever, neck stiffness, fever, trauma, incontinence, tongue biting, recent illness, new meds, missed meds, ETOH/drug use}. Hx ___ {seizure disorder, prior CVA, dementia, diabetes mellitus, psych, ETOH}. Anticoagulated [Y ___ / N].

{Pick the fork that applies. Delete the rest.}

*Seizure:*
Seizure [witnessed by ___ / reported], type ___ {generalized tonic-clonic, focal, absence}, [single / x___ / continuous on arrival], [<5 min / >5 min, ~___ min / status epilepticus]. Postictal on arrival [Y, GCS ___ / N]. Seizure Hx [Y, typical for pt / Y, atypical: ___ / N, first-time]. Meds [compliant / missed ___]. Injuries from seizure ___.
Midazolam [10 mg IM / 10 mg IN / 5 mg IV] for [active seizure / recurrent without return to baseline], seizure [stopped / continued, repeat dose ___] / withheld: ___ {self-terminated, postictal only}. {Pregnant or ≤6 wks postpartum: OB block, mag per pre-eclampsia/eclampsia protocol.}
Recovery: GCS ___ to ___.

*Syncope / near-syncope:*
Event [witnessed / unwitnessed], [prodrome ___ / none], duration of LOC ___, [return to baseline / persistent ___]. Position at onset ___ {standing, seated, exertional, straining}. 12-lead: ___ {rhythm, intervals, blocks, WPW, Brugada, prolonged QT, or "no acute changes"}. Orthostatics [___ supine to ___ standing / not obtained: ___]. Injuries from fall ___. {Exertional, cardiac Hx, abnormal 12-lead, or age >65: name it as the reason for ALS.}

*AMS / unresponsive:*
Hypoglycemia [ruled out, BGL ___ / treated, see Metabolic block]. Opioid toxidrome [absent / present: ___, see Tox block]. Naloxone ___ mg [IN / IM / IV] for RR ___ {only for respiratory insufficiency}, response ___ / withheld: ___ {respirations adequate}. Airway [self-maintained / NPA / OPA / positioned]. Trauma [none evident / ___, see Trauma block]. Sepsis screen [negative / positive, see Metabolic block]. Post-ictal state [considered / ___]. 12-lead: ___. {If none of the above explains it, say so: "no reversible cause identified in the field."}

*Headache / dizziness:*
Headache: onset ___, [thunderclap / gradual], severity ___/10, [worst of life Y/N], with [visual change / neck stiffness / fever / neuro deficit / none]. BP ___.
Dizziness: [vertigo (spinning) / lightheadedness / disequilibrium], [positional / constant], with [nystagmus / ataxia / dysmetria / diplopia / dysarthria / none] {any of these with a normal stroke screen still gets "posterior circulation not excluded" in DDx}.

IV ___g ___. Treatments per fork above. Pt reassessed: GCS ___, NYS-LAMS [unchanged ___ / ___].
**Escalation line:** Stroke screen [negative on initial and reassessment, no focal deficit, LKW ___ / POSITIVE, NYS-LAMS ___/6, LKW ___ per ___, stroke alert called to ___. NYS-LAMS 0-3: NYS-designated stroke center ___. NYS-LAMS 4-6: exclusion criteria reviewed ___, routed to thrombectomy-capable center ___. SBP maintained >120 / SBP ___ >220, med control contacted. Switch to Stroke/CVA template.]

---

## 5. TRAUMA GENERAL BLOCK
Categories: Assault, Fall Victim, Industrial Accident, Pain (Traumatic), Traffic Accident
Escalates to: Trauma Major block on any RED criterion, or a discretionary trauma alert. YELLOW criteria alone: pt goes to a trauma center, documented here, block stays General. Cardiac Arrest template (trauma addendum) if pulses lost.

MOI: ___ {fall from ___ ft onto ___, MVC ___ mph, restrained/unrestrained, airbag, intrusion ___, ejection, rollover, windshield/steering wheel deformity, assault with ___ to ___, machinery ___}. Time of injury ___. [Helmet / seatbelt / PPE] {any that apply} [Y / N / unknown]. Ambulatory on scene [Y / N]. {Elderly, anticoagulated, or intoxicated: say so here, it changes the triage math.}
GCS ___ (E___ V___ M___), pupils ___. Pt [denies / reports] head, neck, or back pain. Distracting injury [Y ___ / N]. Intoxication [Y / N].
[no DCAP-BTLS observed head-to-toe / DCAP-BTLS +]. Injuries found on exam: ___ {by region, head to toe, with side. "Contusion L lateral chest wall, no crepitus, no paradoxical movement." Or "No injuries found."} Distal PMS [intact x4 / ___].
Hemorrhage control: [none required / direct pressure ___ / pressure dressing / hemostatic gauze packed ___, pressure held ___ min / tourniquet ___ 2-3 in proximal, time written on TQ, second TQ]. TQ conversion [not attempted / attempted: pressure dressing applied, windlass released, ___ {no rebleed, TQ left in place loose / rebleed, re-tightened}]. Estimated blood loss ___.
Splinting: ___ {what, how, PMS before and after} / not indicated.
Analgesia {one narcotic on standing order}: fentanyl ___ mcg [IV / IM / IN] / morphine ___ mg / ketamine [25 mg IV over 5 min / 50 mg IM] / acetaminophen 1000 mg PO / ketorolac 15 mg [IV / IM], pain ___/10 to ___/10 / withheld: ___ {pain controlled, SBP, AMS, pt declined}.
IV ___g ___. Fluids [none / ___ mL NS for SBP ___, reassessed ___].
Field triage criteria reviewed: RED [none / ___]. YELLOW [none / ___ {high-risk auto crash: ejection, intrusion >12 in occupant or >18 in any site, extrication, death in compartment, telemetry; rider separated with significant impact; ped/bike thrown or run over; fall >10 ft; EMS judgment: low-level fall ≥65 or ≤5 with head impact, anticoagulant use, pregnancy >20 wks, burns with trauma}].
**Escalation line:** [No RED or YELLOW criteria, trauma alert not indicated, txp to ___ / YELLOW criteria only (___), txp to trauma center ___ / RED criterion MET: ___, switch to Trauma Major block.] {Discretionary: "Trauma alert called at provider discretion for ___."}

---

## 6. TRAUMA MAJOR BLOCK
Categories: Head Injury, Stab/Gunshot Wound, Traumatic Injury, Hanging/Strangulation/Asphyxiation, plus anything from Trauma General meeting a RED criterion or getting a discretionary alert
Escalates to: Cardiac Arrest template with trauma addendum if pulses lost. Neuro block does not apply; head injury findings live here.
{Order matters in this block: it reads as the MARCH sequence because that's the order you did it in.}

MOI: ___ {as Trauma General, plus for penetrating: weapon, number of wounds, entrance/exit if known; for hanging: ligature type, suspension time, drop height, who cut down}. Time of injury ___. LOC [Y ___ min / N / unknown].
RED criteria MET: ___ {name them: penetrating head/neck/torso/proximal extremity; skull deformity or suspected fx; spinal injury with new motor/sensory loss; chest wall instability or flail; suspected pelvic fx; 2+ proximal long bone fx; crushed/degloved/mangled/pulseless extremity; amputation proximal to wrist/ankle; bleeding requiring TQ or packing with continuous pressure; motor GCS <6; RR <10 or >29 or respiratory support; RA SpO2 <90%; SBP <90 (10-64 yo) or <110 (≥65) or HR > SBP; or provider discretion ___}. Trauma alert called to ___. Destination: highest-level trauma center available: ___.
GCS ___ (E___ V___ M___), pupils ___. {Head injury: repeat GCS ___; any drop of 2 or more gets its own sentence.}

Massive hemorrhage: [none / ___ {site}, controlled with ___ {TQ, time written on TQ, wound packing, pressure dressing, junctional}, estimated blood loss ___].
Airway: [patent, self-maintained / ___ {NPA, OPA, suction for ___, positioned}]. {Advanced airway: device, size, attempts, confirmation by ETCO2 ___ and ___, secured at ___ cm.}
Respirations: L/S ___ bilaterally, chest [symmetric / ___ {paradoxical, crepitus, open wound}]. Occlusive dressing to ___. Needle decompression ___ side, ___ ICS ___ line, [rush of air / SBP ___ to ___] / not indicated: ___. SpO2 ___, ETCO2 ___.
Circulation: radial pulse [present / absent], SBP ___, MAP ___, skin ___. IV/IO ___g ___, second access ___. NS 500 mL bolus for SBP <100 / MAP <65, reassessed SBP ___, L/S ___, repeated ___ {to 2 L max while L/S clear, goal SBP ≥100 / MAP ≥65}. TXA 2 g in 100 mL over 10 min for traumatic hemorrhage with SBP <100 / withheld: ___ {SBP ≥100}. Pelvic binder for ___ / not indicated.
Head/spine: spinal motion restriction via ___. Pupils ___, [PEARL / unequal ___], posturing [none / decorticate / decerebrate]. Signs of basilar skull fx [none / fluid from L ear / fluid from R ear / halo sign / Battle sign / raccoon eyes] {any that apply; none is exclusive by convention}. Anticoagulated [Y ___ / N]. {Herniation signs: hyperventilation to ETCO2 ___, or say not indicated.}
Hypothermia prevention: ___ {blankets, heat on, wet clothing removed}.
Injuries found on exam: ___ {head to toe, by region, with side}. Distal PMS ___.
{Hanging/strangulation add:} Ligature marks ___, petechiae [face / conjunctiva / none], voice change [Y / N], stridor [Y / N], subcutaneous emphysema [Y / N]. C-spine ___. {Airway swelling is delayed; say you reassessed it.}
Splinting ___. Analgesia: fentanyl ___ mcg ___ / ketamine ___ mg ___, pain ___ to ___ / withheld: ___ {SBP, GCS, airway}.
Pt reassessed: GCS ___, SBP ___, SpO2 ___, ETCO2 ___, hemorrhage control [bleeding controlled / ___].
Destination ___ {Level I / II trauma center, name}, [by ground / air, ___ requested, landed]. Scene time ___ min {if >10 min, say why in one clause}.
**Escalation line:** Pulses [maintained throughout / LOST. Switch to Cardiac Arrest template, trauma addendum.]

---

## 7. TOX BLOCK
Categories: Alcohol Related, CO Poisoning/Hazmat, Drug or Substance Use/Abuse, Ingestion/Poisoning, Overdose, Radiological Injury, Toxic Exposure
Escalates to: Respiratory Arrest or Cardiac Arrest template. Neuro block if AMS persists after reversal with no tox explanation. Behavioral block for intentional ingestion once medically stable.

Substance ___ {name, or "unknown"}, [ingested / injected / inhaled / dermal / ___], amount ___ {count, mL, bags}, time ___ {or "unknown, last seen normal ___"}, [intentional / accidental / recreational / unknown]. Co-ingestants [ETOH ___ / ___ / none reported]. Source of Hx [pt / bystander / pill bottles ___ {name, count remaining, fill date} / paraphernalia ___ / none]. {Bring the bottles.}
Toxidrome: [opioid: pinpoint pupils, RR ___, ___ / sympathomimetic: ___ / anticholinergic: ___ / sedative: ___ / cholinergic: ___ / none identified]. GCS ___, pupils ___, RR ___, SpO2 ___, ETCO2 ___, BGL ___, temp ___, skin ___.
12-lead: ___ {QRS width, QTc, rhythm; say the number for TCA/sodium-channel and QT-prolonging agents}.
Airway [self-maintained / NPA / OPA / BVM for RR ___ or ETCO2 ___]. O2 ___.

{Pick the fork that applies. Delete the rest.}

*Opioid:*
Naloxone ___ mg [IN unit dose / IM / IV in ≤0.5 mg increments] by [bystander / PD / VAC / 35M___] for RR ___ {given only for respiratory insufficiency or arrest; max 2 mg/dose IV or IM, 4 mg IN}, response: [RR ___ to ___, GCS ___ to ___ / no response, repeat dose ___ mg] / withheld: ___ {respirations adequate, airway self-maintained}. Titrated to respiratory effort, not wakefulness. Not given after advanced airway placed. Pt [cooperative / agitated / withdrawal sx ___] after reversal. Pt advised naloxone wears off before; [accepts txp / see RMA].

*ETOH:*
Pt [ambulatory with assistance / unable to ambulate], speech ___, odor of ETOH [Y / N], last drink ___, [known ETOH Hx / withdrawal Hx / seizure Hx]. Head injury [none evident / see Trauma block]. BGL ___. {The chart has to show you looked for the thing that isn't ETOH: head injury, hypoglycemia, sepsis, stroke.}

*Sedative / unknown ingestion:*
Supportive care. Airway as above. Poison Control [contacted, ref ___, recommendations ___ / not contacted: ___]. Activated charcoal [not given / ___ per med control].

*Sympathomimetic / agitated:*
Agitation: verbal de-escalation attempted ___ [effective / ineffective], environmental modification ___, danger to [self / crew / public]. BGL ___ when safe. Midazolam ___ mg [IM / IV] / olanzapine [10 mg IM / 5 mg SL / 2.5-5 mg IM if ≥65] / ketamine 250 mg IM for ___ {clinical triad: psychomotor agitation, physiologic excitation, failed de-escalation, with ___ of: unusual strength, no tiring, pain tolerance, tachypnea, diaphoresis, hyperthermia, AMS} / withheld: ___. Response: ___. Airway, SpO2, ETCO2 monitored continuously after sedation: ___. Temp ___ {hyperthermia treated with ___}. Restraints [none / soft, ___ points, applied by ___, supine, PMS checked q___, reason ___]. Pt not transported prone. PD [on scene / requested].

*CO / hazmat / inhalation:*
Scene [safe / hazmat staged / ___ metered ___ ppm by ___]. Exposure duration ___, others exposed ___. SpCO ___ if available. High-flow O2 NRB 15 LPM. Symptoms ___ {headache, N/V, confusion, syncope, CP}. Decon [performed by ___ / not required]. Destination [hyperbaric-capable ___ / ___].

*Cholinergic / organophosphate:*
SLUDGE findings ___. Decon. Atropine ___ mg, repeated ___, secretions [drying / ___]. DuoDote/pralidoxime ___ / not available.

*Radiological:*
Per hazmat/IC direction ___. Decon ___. Contamination survey ___. Treated as trauma/medical per presenting problem, see ___ block.

Pt reassessed: GCS ___, RR ___, SpO2 ___, ETCO2 ___. Police [on scene / notified / not involved].
**Escalation line:** Pt [maintained adequate respirations and pulses throughout / respirations became inadequate, BVM initiated, switch to Respiratory Arrest template / pulses lost, switch to Cardiac Arrest template].

---

## 8. METABOLIC / SEPSIS BLOCK
Categories: Diabetic Problem, Fever/Sepsis
Escalates to: Neuro block if AMS persists after glucose corrected. Respiratory block if the source is pulmonary and needs its own treatment.

*Hypoglycemia:*
BGL ___. Pt [responsive, able to swallow / AMS, GCS ___ / unresponsive]. Last meal ___, last insulin/oral agent ___ {name, dose, time}, [usual regimen / recent change / missed meal / increased activity / ETOH]. Prior episodes [Y / N].
Oral glucose ___ g {15-30 g, able to swallow on command} / D10 ___ mL IV {up to 25 g / 250 mL} / glucagon 1 mg IM (IV unobtainable x___). Repeat BGL ___, GCS ___ to ___. D10 redosed ___ mL for recurrence / not required.
Pt [ate ___ after recovery / declined food]. Sulfonylurea or long-acting insulin on board [Y ___, recurrence risk explained / N]. {This line is what makes or breaks the RMA on a diabetic.}

*Hyperglycemia / DKA:*
BGL ___ [High (over range)]. Kussmaul respirations [Y / N], fruity odor [Y / N], polyuria/polydipsia ___ days, N/V ___, abd pain ___. Skin ___, mucous membranes ___. ETCO2 ___. 12-lead: ___ {peaked T's, rhythm}. Insulin compliance ___, [pump: ___ / new dx]. IV ___g ___, NS ___ mL, reassessed ___.

*Sepsis:*
Suspected source ___ {UTI, pneumonia, skin/wound, indwelling line/catheter, post-op, unknown}. Onset ___. Immunocompromised [Y ___ / N]. Facility/family reports ___.
Sepsis screen: suspected infection [Y ___ / N] with [SBP <100 / AMS / neither]. Indicators: temp ___, HR ___, RR ___, ETCO2 ___, [fever, chills, diaphoresis, new cough, urinary sx, new AMS, flushed, pallor, rash, mottling]. [Meets septic shock criteria / suspected infection, criteria not met]. Skin ___, cap refill ___.
Large-bore IV ___g ___, second access ___. NS 500 mL bolus for SBP <100 / MAP <65, reassessed SBP ___ to ___, MAP ___, L/S ___ {repeat to 2 L while clear, goal SBP >100 / MAP >65; stop and say so if rales develop}, repeated, ___. O2 NRB. Hospital notified of suspected septic shock / not indicated: ___.
Norepi started at ___ {2-20 mcg/min, after ≥1 L in, to MAP >65 / SBP >100} mcg/min, titrated to ___, MAP ___ to ___ / not indicated: ___.

Pt reassessed: BGL ___ / SBP ___, MAP ___, GCS ___.
**Escalation line:** [Hypoglycemia corrected, BGL ___, pt at baseline / BGL corrected but AMS persists, GCS ___, no other cause identified, see Neuro block] / [Sepsis screen negative / Sepsis screen POSITIVE, alert called, fluids as above].

---

## 9. GENERALIZED MEDICAL BLOCK
Categories: Abnormal Labs, General Illness/Malaise, Hypertension (a-symptomatic), Sick Person, Unable to Ambulate, Weakness, Fever/High Temperature
This is the block for "nothing specific." Its whole job is to prove the specific things were screened for and were negative. Escalates to whichever block the screen turns up.

Pt reports ___ {in their words: weak, tired, "not right," can't get up}, onset ___ {hours/days}, [gradual / sudden], [progressive / static]. Associated ___ {fever, chills, cough, dysuria, N/V/D, poor PO intake ___ days, falls, dizziness, CP, SOB, new meds, missed meds}. Last seen at baseline ___ per ___. Baseline function ___ {independent, walker, bed-bound}. Living situation ___ {alone, with family, facility}.
Screens: BGL ___. Temp ___. Sepsis screen [negative / positive, see Metabolic block]. 12-lead [___ / not indicated: ___]. NYS-LAMS [0, no focal deficit / see Neuro block]. Orthostatics [___ / not obtained: ___]. Hydration: mucous membranes ___, skin turgor ___, urine output per pt ___.
{Fever/High Temp:} Temp ___, duration ___, [localizing sx ___ / none], sick contacts ___, antipyretics taken ___ at ___. Sepsis screen as above.
{Asymptomatic HTN:} BP ___ x___ readings, pt denies headache, vision change, CP, SOB, neuro sx. Neuro exam grossly intact. Med compliance ___. No treatment indicated; pt advised private medical doctor follow-up within ___.
{Abnormal labs:} Sent by ___ {private medical doctor, dialysis, facility} for ___ {lab, value, drawn ___}. Pt [symptomatic ___ / asymptomatic]. 12-lead: ___ {mandatory for K, Ca, Mg, dig}. Treatment ___ / none indicated in the field.
{Unable to ambulate:} [Weakness / pain ___ / mechanical: ___]. Injuries [none / see Trauma block]. Lift assist only [Y, pt assessed and at baseline / N]. Skin check [intact / ___] if down time >1h. Creatine kinase-relevant down time ___.
IV ___g ___ / not indicated. Fluids ___ mL NS for ___ / none.
Working impression ___ {"generalized weakness, etiology unclear, dehydration vs UTI vs ___"}.
Pt reassessed: ___.
**Escalation line:** Screens negative for hypoglycemia, sepsis, stroke, and acute cardiac cause; pt txp for ___ / [screen POSITIVE for ___, see ___ block].

---

## 10. ABDOMINAL / GI BLOCK
Categories: Abdominal Pain, GI Bleed, Nausea/Vomiting, Pain (Non-cardiac)
Escalates to: Metabolic/Sepsis block if septic; Cardiac 2a if epigastric pain is cardiac-suspicious (>35 yo, risk factors, diaphoresis); OB block if pregnant; Trauma if traumatic.

Pain: ___ {OPQRST, location by quadrant, radiation to back/groin/shoulder, quality}. Associated [N/V ___ episodes / diarrhea / constipation, last BM ___ / fever / urinary sx / melena / hematemesis ___ {coffee-ground, bright red, volume} / hematochezia / none] {any that apply}. Last oral intake ___. {Female of childbearing age: last menstrual period ___, pregnancy [possible / denied].}
Abd exam: [soft / rigid / guarded], [non-tender / tender ___ quadrant], [distended / non-distended], [rebound tenderness / none], [pulsatile mass / none]. {>50 with back/abd pain: bilateral femoral pulses ___, "AAA not excluded" in DDx if any asymmetry or hypotension.}
{GI bleed:} Skin ___, orthostatics ___, anticoagulated [Y ___ / N], prior GI bleed [Y / N], ETOH Hx [Y / N]. Estimated blood loss per pt/scene ___.
12-lead for epigastric/upper abd pain: ___ / not indicated: ___.
IV ___g ___. NS ___ mL for ___, reassessed ___ / none.
Ondansetron ___ mg [ODT / IV / IM] for ___ / isopropyl pad self-inhalation / withheld: ___.
Analgesia: fentanyl ___ mcg, pain ___ to ___ / withheld: ___ {no ketorolac/ibuprofen for abd pain: bleeding risk}.
**Escalation line:** [No peritoneal signs, hemodynamically stable throughout / sepsis screen positive, see Metabolic block / hypotensive with GI bleed: ___ {fluids, goal}, hospital notified of unstable GI bleed].

---

## 11. ALLERGIC BLOCK
Categories: Allergic Reaction
Escalates to: Respiratory Arrest template. Respiratory block for isolated bronchospasm without systemic signs.

Exposure: ___ {allergen, route, time}. Prior anaphylaxis Hx [Y, to ___ / N]. Epi auto-injector [used prior to arrival at ___ / prescribed, not used / none].
Presentation: [rash/hives ___ distribution / itching / facial or oral edema ___ / stridor / wheezing / resp distress / hypotension SBP ___ / GI sx: N/V, abd pain, diarrhea / ___]. [ANAPHYLAXIS: severe resp distress, facial/oral edema, or hypoperfusion, OR Hx of anaphylaxis + exposure + (resp distress / hypoperfusion / rash) / allergic reaction, systemic criteria not met].
Epi 0.3 mg (1 mg/mL) IM, response: ___ / withheld: ___ {criteria not met}.
Albuterol 2.5 mg / ipratropium 0.5 mg neb for wheezing, x___ / withheld: ___.
IV ___g ___. NS 500 mL bolus for SBP <100 / MAP <65, reassessed ___, repeated ___ {to 2 L, L/S clear} / none.
Diphenhydramine 50 mg [IV / IM] / withheld: ___. Dexamethasone 10 mg [PO / IM / IV] / withheld: ___.
Epi infusion started at ___ {start 5, titrate to MAP >65 / SBP >100} mcg/min, titrated ___ / not indicated.
Pt reassessed: airway ___, L/S ___, SBP ___, rash ___.
**Escalation line:** [Symptoms improving, airway patent throughout / airway compromise progressed, ___. Switch to Respiratory Arrest template.] {Epi given + pt wants to refuse: med control per regional procedure, cite above.}

---

## 12. BEHAVIORAL BLOCK
Categories: Anxiety, Psychiatric Problems
Escalates to: Tox block for ingestion; Neuro block if medical cause suspected; the agitated-patient fork in Tox for chemical restraint (same documentation either way).

Presentation: ___ {in pt's words and observed affect/behavior}. [Danger to self: ___ / danger to others: ___ / neither expressed or observed] {any that apply}. SI [denied / expressed: ___ {plan, means}]. Homicidal ideation [denied / expressed: ___].
Medical screen: BGL ___, [no evidence of trauma, intoxication, hypoxia, or acute medical cause / ___]. Psych Hx ___ {dx, meds, compliance ___, prior admissions}. Recent stressors/changes ___.
De-escalation: [verbal effective, pt cooperative / ___]. PD [on scene / requested / not needed]. {Mental Hygiene Law status if applicable: 9.41 by PD, 9.45 by Director of Community Services, or voluntary. Involuntary transport: capacity determination and PD role documented plainly.}
Restraints [none / soft ___ points by ___, supine, PMS q___, reason: ___]. Sedation [none / see Tox agitated fork, documented there].
Pt transported [voluntarily / involuntarily under ___] to ___ {Comprehensive Psychiatric Emergency Program-capable ED if that drove the destination}.
**Escalation line:** Pt remained [calm and cooperative / ___] throughout. Medical causes screened: BGL ___, no acute medical findings / [medical cause suspected: ___, see ___ block].

---

## 13. BURNS / ELECTRICAL BLOCK
Categories: Burns, Electrocution
Escalates to: Trauma Major on any RED criterion (burns + trauma go to trauma center). CO/hazmat fork of Tox for inhalation. Cardiac 2b for post-electrical dysrhythmia. Cardiac Arrest template if pulses lost.

Source: ___ {flame, scald, chemical ___, electrical ___ V AC/DC, contact time ___, lightning}. Enclosed space [Y, duration ___ / N]. Burning stopped by ___. Scene [safe / utility secured by ___].
Burns: ___ {degree, location, circumferential Y/N}, ___% BSA (rule of nines: ___) {first-degree excluded from BSA}. Airway: [no facial burns, singed nasal hair, soot, or voice change / ___: airway burn suspected]. {CO considered: SpCO ___ / see Tox CO fork.}
{Electrical:} Entry ___, exit ___, [LOC / tetany / fall from ___]. Monitor: ___ {rhythm; dysrhythmia → add Cardiac 2b}. 12-lead: ___. {Lightning/high voltage: c-spine per Trauma criteria.}
Rings/constricting items removed. Dressings: [dry sterile / moist sterile (≤10% BSA, for pain)]. {Chemical: flushed ___ min with ___; dry powder brushed first.} {Eye: irrigated with NS, copious; tetracaine 2 gtt q5 prn.}
IV ___g ___ x [1 / 2]. NS 500 mL bolus, reassessed ___. Hypothermia prevention ___ {>10% BSA: dry dressings only, pt kept warm}.
Analgesia: fentanyl ___ mcg, pain ___ to ___ / ketamine ___ / withheld: ___.
Destination: [ED ___ / trauma center (burns + trauma) / burn center per med control, cited above].
**Escalation line:** [Airway patent and voice unchanged throughout, rhythm ___ / airway involvement progressed / dysrhythmia ___, see Cardiac 2b. RED criteria: none / MET ___, Trauma Major.]

---

## 14. DOA BLOCK
Categories: DOA (attended), DOA (Unattended)
No escalation. If criteria are NOT met, this block does not apply: work the arrest on the Cardiac Arrest template.

Found: ___ yo [M/F] [in bed / ___], last known alive ___ per ___. Pt pulseless and apneic.
Obvious death criteria: ___ {ANY one, name what you saw: body decomposition / rigor mortis / dependent lividity / injury incompatible with life: ___ / pulseless + apneic with no organized activity on ECG after significant blunt or penetrating trauma meeting RED criteria / submersion >1 hr} OR valid [MOLST / eMOLST / DNR] presented, verified by ___ {form location, signatures}.
{ALS strip if used:} Monitor applied: [asystole confirmed in ___ leads / no organized activity], strip attached. {Not required for obvious-death criteria; say why no strip if none.}
Resuscitation [not initiated / initiated by ___ and discontinued per criteria above; pads and equipment left in place].
{Hypothermia caveat: criteria differ in severe hypothermia; if cold, say why criteria still applied or why you worked it.}
PD notified, [on scene / ETA ___]. Scene [undisturbed / pt covered / moved to ___ with PD permission]. {Attended:} Pt under care of [hospice ___ / MD ___], ___. Family on scene: ___, informed by ___.
35M___ [remained on scene / released by PD]. 35M___ returned to service.
{This block replaces the treatment sections AND the disposition. Nothing else follows it.}

---

## 15. ENVIRONMENTAL BLOCK
Categories: Drowning, Heat/Cold Exposure
Escalates to: Cardiac Arrest template (hypothermic arrest: say resuscitation continued, cold caveats applied). Respiratory block for post-drowning respiratory distress. Trauma if mechanism involved.

Exposure: ___ {environment, temp if known, duration, wet/dry, clothing}. Found by ___.

{Heat, normal mental status:} Skin [elevated temp / normal], clothing loosened, [oral hydration / cold packs to palms, soles, neck, groin, axillae, skin kept wet].
{Heat, AMS:} Elevated skin temp with GCS ___: active whole-body cooling initiated via ___ {in order of preference: ice/cold water immersion, TACO, cold dousing, cold-soaked towels + ice packs}, continued until mental status returned / continued through txp. {Transport delayed for cooling: say so and why, it's protocol.} NS 500 mL bolus, repeated ___ {to 2 L, no pulmonary edema}.
{Cold:} Core/axillary temp ___ if obtained. [Mild: shivering, alert / moderate: ___ / severe: ___]. Wet clothing removed, passive rewarming ___, handled gently {rough handling → VF}. [Localized: part ___, [rewarmed with ___ / not field-rewarmed: refreezing risk], not rubbed].
{Drowning:} Submersion ___ min in ___ {water type/temp}, [witnessed / unwitnessed], extricated by ___ at ___. [Breathing on our arrival / resuscitated by ___]. L/S ___, SpO2 ___, ETCO2 ___. [C-spine per criteria: ___]. {Every symptomatic submersion gets transport advised: delayed pulmonary edema named in the RMA risk line if pt refuses.}
Pt reassessed: GCS ___, temp trend ___, L/S ___.
**Escalation line:** [Stable/improving throughout / deteriorated: ___. Switch to ___ template.]

---

## 16. NON-CLINICAL BLOCK
Categories: Not Applicable, Not Known, Other, Unknown Problems, Welfare Check
The job of this narrative is to prove there was no patient, or why no assessment happened. Short is correct; missing is not.

35M___ [dispatched for ___ / requested by ___ to stand by at ___].
On arrival: ___ {what was found, in one or two sentences}.
[No patient found after search of ___ with ___ {PD, FD} / subject ___ located, denies injury or illness, no visible distress, ambulatory, declines assessment: see RMA / no EMS role: ___ {matter handled by PD, lockout, paperwork call} / staged at ___ from ___ to ___, not committed, no pt contact].
{Welfare check with subject found down or ill: this block does not apply. Use the clinical block for what you found.}
Agencies on scene: ___. Command/IC if established: ___.
Disposition 3 (cancelled) or RMA per shell. 35M___ returned to service.

---

## 17. OB BLOCK
Categories: Pregnancy/Childbirth. Cross-reference: Seizure (Neuro) in pregnancy or ≤6 wks postpartum lands here.
Escalates to: Neuro/Seizure for the seizure mechanics; OB Hemorrhagic Shock lines below for postpartum bleeding; Cardiac Arrest template if pulses lost (note leftward uterine displacement during CPR).

G___ P___, ___ wks by [dates / ultrasound / pt report], prenatal care [Y, ___ / N]. Complications this pregnancy ___ {HTN, gestational diabetes mellitus, previa, multiples}. {>20 wks: pt positioned left lateral recumbent / uterus manually displaced leftward.}
Presenting: ___ {contractions q___ min x ___ sec since ___, rupture of membranes at ___ [clear / meconium], bleeding ___, urge to push [Y/N], fetal movement ___}.
{Pre-eclampsia screen, >20 wks to 6 wks postpartum:} BP ___ [≥160/110 / 140-159 or 90-109 with: severe headache / visual changes / RUQ or epigastric pain / none]. [Screen negative / PRE-ECLAMPSIA: mag 4 g in 100 mL IV over 20 min started] [ECLAMPSIA, seizing: mag as above + Neuro seizure fork, midazolam documented there].
{Delivery imminent:} Crowning noted. Delivery: [vertex / ___], nuchal cord [none / reduced x___], infant [suctioned as needed / stimulated], APGAR ___ at 1 min, ___ at 5 min. Cord clamped and cut. Placenta [delivered, transported / undelivered].
{Postpartum hemorrhage:} estimated blood loss ___, [firm fundus after massage / boggy]. Fundal massage performed. {Per OB Hemorrhagic Shock protocol:} NS bolus ___. Oxytocin not carried; med control contacted for ___ / TXA ___ per med control. SBP ___ to ___.
Two patients documented from delivery forward: [infant assessment in linked PCR ___ / infant care transferred to ___].
**Escalation line:** [Uncomplicated, mother and infant stable / pre-eclampsia treated as above, BP ___ on reassessment / postpartum hemorrhage: interventions above, hospital notified of unstable OB]. Destination [ED / L&D-capable ___ per ___].

---

## 18. POLICE ASSIST BLOCK
Categories: Blood Draw Request, Law Enforcement Blood Draw, Medication Administration (Assist PD), EMS Requested by Law Enforcement
The chart here is as much legal record as medical record. Times, names, badge numbers, and what was NOT done carry the weight.

Requested by [___ PD, Officer ___, badge ___] for ___.
{LE blood draw:} Draw performed under [pt consent, witnessed by ___ / court order presented, reviewed / ___ per agency policy]. Pt [cooperative / ___]. Site ___ cleaned with [non-alcohol prep ___]. Kit: [PD-supplied kit, sealed, lot ___], tubes x___, handed directly to Officer ___, chain of custody form [signed / ___]. No medical complaint voiced; [assessment offered and declined, see RMA / assessed: ___].
{Medication administration assist:} Medication ___ administered under ___ {standing order / med control Dr. ___}, indication ___, response ___. Custody status ___. Documented assessment before and after: ___.
{EMS requested by LE, subject in custody:} Subject assessed: ___ {injuries or complaints, or "denies injury or complaint"}. [Tase/OC/restraint exposure: probes removed by ___, sites ___, ___]. [Fit for incarceration NOT determined by EMS; pt advised and PD advised transport available / pt transported / RMA with PD witness ___].
**Escalation line:** [No medical complaint identified, no treatment indicated / clinical issue found: ___, see ___ block].

---

## 19. TRAUMA MINOR / MUSCULOSKELETAL BLOCK
Categories: Animal Bite, Back Pain, Eye Problem, Foot Injury, Fracture/Dislocation, Hemorrhage/Laceration, Pain (extremities), Soft Tissue Injury
Escalates to: Trauma General/Major if MOI or findings say so (field triage criteria reviewed and negative is the load-bearing line here).
{Spinal motion restriction/c-spine: covered by the shell Primary line for this block.}

MOI: ___ {low-energy, in one clause}. Time of injury ___.
Injury: ___ {what, where, side, size for wounds}. Distal PMS [intact / ___] before and after any splint. [Deformity / swelling / ecchymosis / wound edges ___ / none] {any that apply}.
{Bite:} Animal ___, [provoked / unprovoked], owner ___ {known, vaccination status ___ / unknown/stray}, [animal control / PD] notified. Wound irrigated with ___.
{Eye:} Visual acuity [grossly intact / ___], [no globe injury evident / ___]. Irrigation ___ / tetracaine 2 gtt / not indicated. {Penetrating globe: no pressure, shield, escalate.}
{Back pain, atraumatic red flags screened:} [no saddle anesthesia, no new incontinence/retention, no bilateral leg weakness, no fever, no anticoagulants, no cancer Hx / ___: escalate DDx].
Wound care: [irrigated / dressed ___ / bleeding controlled with direct pressure]. Splint: ___ {type, position}, PMS rechecked ___ / not indicated.
Analgesia: [acetaminophen 1000 mg PO / ibuprofen 400 mg PO {not if >60, anticoagulated, renal, pregnant} / ketorolac 15 mg {same limits} / fentanyl ___ mcg / none, pain ___/10, pt declined].
Field triage criteria reviewed: [no RED or YELLOW criteria].
**Escalation line:** [Isolated ___ injury, no triage criteria met / criteria MET: ___, see Trauma General/Major].

---

# DEDICATED TEMPLATES
Full narratives. The shell's dispatch/arrival opening and disposition close still wrap them; the template replaces everything in between. Doses per v26.1.

## 20. TEMPLATE: CARDIAC ARREST (medical)
{Also the base for Traumatic Arrest: complete this template and add section 20a.}

Arrest [witnessed by ___ at ___ / unwitnessed, last known alive ___ per ___]. Estimated downtime ___. Bystander CPR [by ___ from ___ / none]. AED [applied by ___, ___ shocks delivered / none] prior to arrival.
Upon 35M# arrival: pt pulseless, apneic. Obvious death criteria reviewed: not met {if met, this is the DOA block, stop}. [DNR/MOLST: none presented / presented and did not preclude resuscitation: ___].
Compressions [continued / initiated]. Initial rhythm on monitor: [VF / pulseless VT / asystole, confirmed in ___ leads / PEA, rate ___].
CPR per AHA: 100-120/min, rotated q2 min, interruptions minimized, mechanical CPR device [applied by ___, rate set to 30:2 / Continuous].
Defibrillation: ___ J {each shock}. [Vector change to anterior/posterior for refractory VF/VT / n/a].
Airway: [OPA/NPA + BVM with O2 / iGel ___ / ETT ___, ___ attempts, depth ___ cm], placement confirmed by waveform capnography, ETCO2 ___. After advanced airway: continuous compressions, 8-10 breaths/min.
Access: [IV ___g ___ / IO ___]. BGL ___.
Epi 1 mg (0.1 mg/mL) IV/IO.
{Shockable:} [Amiodarone 300 mg IV / Lidocaine ___ mg IV {1.5 mg/kg}, repeat ___ mg {0.75 mg/kg}]. {Torsades/hypomag:} Mag 2 g IV.
{PEA/asystole:} NS 500 mL bolus. {Suspected hyperkalemia (dialysis, Hx):} Sodium bicarb 50 mEq IV, calcium chloride 1 g IV, ≥50 mL NS flushed between.
Reversible causes addressed: ___ {H's & T's actually searched: BGL ___, volume ___, hypoxia ___, tension pneumo [decompressed ___ / not suspected], tox ___, hyperK ___}.
Rhythm checks q2 min: ___ {sequence with times, or "per code summary, attached"}. {Monitor data/code summary attached, as with every assessed or treated pt.}

[ROSC: pulses at ___, rhythm ___, BP ___. 12-lead: ___ {STEMI → PCI-capable destination}, transmitted. NS to maintain SBP >100 / MAP >65: ___ mL, L/S ___. Norepi 2-20 mcg/min started / push-dose epi 10-20 mcg q3-5 / not needed. Sedation for airway per protocol: ___. Re-arrest [none /, resumed above]. Hospital notified of ROSC.]

[No ROSC: TOR criteria: age ≥18 [Y], arrest unwitnessed by bystanders and EMS [Y/N], no bystander CPR [Y/N], no shocks delivered [Y/N], no ROSC at any point [Y/N], ≥20 min resuscitation [Y, ___ min], hypothermia not suspected [Y]. Med control contacted, Dr. ___, criteria reported, orders: [terminate / continue: ___]. {All seven standing-order criteria met and termination on standing order instead: say so.} ETCO2 at termination discussion: ___. Tubes and lines left in place. PD notified. Family present: ___, supported by ___. Pt moved to ___ with PD permission / left in place.]

## 20a. TRAUMATIC ARREST ADDENDUM
MOI: ___ {blunt/penetrating, RED criteria met: ___}. {Blunt or penetrating trauma + no organized activity on ECG = obvious death criterion: if that was the case, DOA block, not this template.}
Organized activity on initial ECG: [Y, rate ___ / N but mechanism inconsistent with traumatic cause, worked as medical].
Trauma-specific interventions, in order done: bilateral chest decompression [___ ICS ___ line R, L, result ___ / not indicated], hemorrhage control ___ {TQ/packing, times}, pelvic binder ___, airway with c-spine ___.
Volume: NS ___ via [IV x2 / IO].
Destination if ROSC: trauma center ___. TOR: traumatic arrests follow the same criteria; med control contact ___ documented above.

## 21. TEMPLATE: STEMI
{Starts as Cardiac 2a; from the moment criteria fire, this replaces it.}

12-lead: ST elevation ___ mm in ___ {leads}, [reciprocal depression ___ / none], [new LBBB]. STEMI identified. {Inferior: R-sided 12-lead: [RV involvement ___ / negative].}
STEMI alert called to ___, [confirmed by Dr. ___ / transmitted, unconfirmed].
Destination: ___ {PCI-capable, ETA ___ min from pt contact; <90 min window [met / not met, med control consulted: ___]}.
Defib pads placed. ASA 324 mg chewed / given prior / withheld: ___.
NTG 0.4 mg SL x___, SBP ___ before each {>120 or MAP >90 required; withheld: ___ {SBP, RV involvement, phosphodiesterase-5 inhibitor}}.
IV ___g ___. {SBP <100: supine, NS 500 mL, repeated ___ {to 2 L, L/S clear, goal SBP >100}.}
Fentanyl ___ mcg for pain ___ unrelieved by NTG, ___ to ___ / withheld: ___.
{Med control adds:} Metoprolol 5 mg slow IV per Dr. ___ {HR >80 and SBP >120} / none.
Serial 12-lead: ___. Reassessed en route q___: pain ___, rhythm ___ {watch for blocks and VF, pads already on}.
Prenote update to ___: ETA ___, [cath lab activated per receiving RN / ___]. {If arrest en route: Cardiac Arrest template from that timestamp.}

## 22. TEMPLATE: RESPIRATORY ARREST / FAILURE
{Apneic or RR <10 / ineffective respirations with a pulse. If pulses lost: Cardiac Arrest template from that timestamp.}

Found: [apneic / RR ___, ineffective: ___ {cyanosis, retractions, AMS}], pulse [present, rate ___]. SpO2 ___, ETCO2 ___.
Airway opened [head-tilt chin-lift / jaw thrust], suctioned ___, [visible obstruction removed: ___ / FBAO suspected → laryngoscopy, Magill, result ___ / clear].
BVM with O2 initiated, q5-6 sec, visible chest rise [Y / difficult: ___]. [OPA / NPA] placed.
Suspected cause: ___ {opioid → naloxone ___ per Tox block dosing, response ___ / CHF / COPD / asthma → see block treatments given: ___ / neuro / other}.
[Ventilation effective with BLS airway, advanced airway deferred / Advanced airway: [iGel ___ / ETT ___, ___ attempts, ___ cm], confirmed by waveform capnography ETCO2 ___ and ___ {auscultation, chest rise}, secured, re-verified after every move: ___.]
Post-airway management: ventilation rate ___, SpO2 ___ to ___, ETCO2 ___ to ___. Sedation/analgesia for airway tolerance: [midazolam ___ / fentanyl ___ / not required: ___] {per post-intubation protocol}.
Reassessed q___: [spontaneous respirations returned, RR ___, supported with ___ / ventilated throughout]. Pulse [maintained / LOST → Cardiac Arrest template].
Hospital notified of [ventilated pt / airway in place], RN ___.

## 23. TEMPLATE: STROKE / CVA
{Neuro block fires positive → this.}

LKW ___ per ___ {name/relationship, contact collected: ___}. Symptom onset ___ if witnessed, by ___. Onset-to-ED estimate ___ {<3.5 hr → NYS-designated stroke center required}.
Deficits found: ___ {each named: facial droop ___ side, arm drift ___, speech ___, gaze, neglect, visual field}.
NYS-LAMS Score: ___/6 {droop ___, drift ___, speech ___, grip ___}.
BGL ___ {<60 treated per Metabolic block: ___, deficits [resolved → not a stroke alert, chart it / persist]}. Anticoagulated [Y ___ / N]. Recent surgery/trauma/GI bleed [___ / none reported]. Seizure at onset [Y / N].
Stroke alert called to ___ with LKW and NYS-LAMS. Destination: [NYS-LAMS 0-3: ___ {NYS stroke center} / NYS-LAMS 4-6: exclusions reviewed, ___ {thrombectomy-capable}], txp decision per ___ {protocol / med control Dr. ___}.
IV ___g ___. SBP ___ [maintained >120 / >220 or DBP >120: med control, orders ___]. Head of stretcher ___. NPO.
Serial neuro: [unchanged / evolving: ___]. {Deficits resolving en route: documented as ___, alert NOT cancelled by EMS.}
Prenote update: ETA, deficits, LKW, family [following / contact ___ given to RN ___].

## 24. TEMPLATE: ACTIVE SHOOTER / VIOLENT INCIDENT
{Operational narrative. Clinical care per patient goes on that patient's PCR with the right block; this template is for the incident-role chart. RTF is regionalized and no county-level plan exists: default posture is staged until PD declares the scene, and this chart documents exactly that.}

35M___ [dispatched / self-dispatched per ___ / other…] to reported active shooter at ___. Staged at ___ {location} per [dispatch / IC / other…]. Scene declared [unsecured / secured / other…] by ___ {PD/IC}.
ICS: incident command ___, 35M___ assigned [staging / casualty collection point at ___ / treatment / transport / other…] by ___. Unified command [Y / N / other…]. MCI [declared, level ___ → MCI template supplements / not declared / other…].
Entry: [remained staged, no pt contact, released / entered warm zone with ___ {LE escort/RTF}, PPE ___].
Care rendered under [TECC/warm zone constraints]: ___ {hemorrhage control, airway positioning, rapid extraction; interventions deliberately deferred to CCP/cold zone: ___}. Pts moved to CCP.
Patients treated/transported by 35M___: ___ {triage tag #s; each gets own PCR, cross-referenced}.
Accountability: both crew accounted for. Released from incident by ___.

## 25. TEMPLATE: MCI
{Incident-role chart. Each transported pt still gets a PCR; abbreviated per MCI standard, cross-referenced by triage tag #.}

MCI declared by ___ for ___ {incident}, estimated ___ pts. Level ___ per ___.
35M___ arrived, assigned [triage / treatment / transport / staging / medical branch] by IC ___.
Triage system: START. Pts triaged by 35M___: ___ {counts by category: Red ___, Yellow ___, Green ___, Black ___}.
{Triage role:} Triage completed, counts reported to ___. No treatment during triage beyond [airway positioning / hemorrhage control] per START: ___.
{Treatment role:} Treatment area, pts received ___, interventions ___ {by tag #}.
{Transport role:} Destinations coordinated with ___ {hospital/MedCom}: ___ {tag # → hospital, ordered by priority}. Hospital capacity confirmed via ___.
Pt(s) transported by 35M___: tag # ___, [category], ___ {one line of clinical course each; full detail in that pt's PCR}.
Documentation standard: abbreviated PCRs per regional MCI procedure, completed [during / after] incident; this narrative cross-references tag #s ___.
Released by ___. Demobilized, returned to service ___.

---

## 26. WORKED SAMPLE: 68 yo M chest pain, no STEMI
{Uses shell + 2a. This is what a finished narrative looks like once the notes are deleted.}

35M3 dispatched to a private residence in the Town of Cortlandt for a 68 yo M with chest pain. 35M3 responded emergency. 35M3 arrived on scene (Cortlandt Community VAC on location) and found 68 yo M pt seated on the edge of his bed, diaphoretic, clutching his chest, in moderate distress.
Pt + patent airway, + breathing w/ initial L/S clear bilaterally, + radial pulse strong and regular, skin pale, cool, diaphoretic. Pt placed on NC 2 LPM by VAC prior to arrival, SpO2 96%.
Pt A&Ox4 (P, P, T, E), A, - LOC, and complaining of "pressure in the middle of my chest" x 45 min, onset at rest while watching TV. Pt states pain radiates to L arm and jaw, 7/10, worse than anything prior, with nausea and one episode of lightheadedness on standing. Wife states pt "looked gray" and took nothing prior to calling 911.
Pt PMHx HTN, hyperlipidemia, type 2 diabetes mellitus, ex-smoker quit 2015, no prior cardiac Hx. Meds per list, compliant. NKDA. Last oral intake dinner 1900. No MOLST.

Vitals as noted in emsCharts activity log, concerning for initial BP 152/90, HR 88, RR 20, SpO2 96% on 2 LPM, BGL 164.

Working impression ACS. DDx unstable angina vs NSTEMI vs aortic dissection vs PE.
Secondary assessment head-to-toe unremarkable except mild diaphoresis, resolved by 2230. Abd soft, non-tender. No pedal edema. Neuro grossly intact.

{The Cardiac block — the only one stacked on this call — is its own paragraph:}
Pt describes substernal pressure, non-reproducible, non-pleuritic, no tearing quality, equal radial pulses bilaterally, no calf tenderness, no recent immobility. Associated diaphoresis, N/V, and lightheadedness. Cardiac risk factors HTN, HLD, DM, former smoker, FHx father MI at 62.
12-lead acquired at 2214: NSR 88, normal axis, intervals WNL, nonspecific T-wave flattening in V5-V6, no ST elevation or depression, no reciprocal changes.
ASA 324 mg PO administered at 2216.
NTG 0.4 mg SL x2 at 2217 and 2223, pain 7 to 3/10, BP 138/84 after second dose.
IV 18g L AC at 2220, saline lock. Fluids none.
Fentanyl withheld: pain improved to 3/10 with NTG, pt declined further analgesia.
Serial 12-lead at 2228: unchanged.
STEMI criteria not met on serial 12-leads.

Pt reassessed en route at 2236: pain 2/10, skin warm and dry, SpO2 97% on 2 LPM. Remaining vitals per activity log.
Pt txp ALS to NYP-HVHC. Hospital notified via cell at 2233. No pt changes throughout txp. Pt transferred to ED staff, report given to RN Martinez. 35M3 returned to service without further incident.

---

## 27. OPEN ITEMS
- v0.8 incorporates your v0.7 answers: "Upon 35M# arrival" voice, mechanical CPR device line, NYS-LAMS as the sole documented stroke scale (Neuro block and Stroke template), TOR via med control contact at the ~20-min mark, postpartum hemorrhage line reflects no oxytocin (med control instead), Morgan Lens and oxymetazoline removed, Active Shooter template defaults to staged-until-declared with the no-county-plan reality noted.
- Resolved: START for MCI; monitor data attached for every pt assessed and/or treated (arrest code summary included).
- One caution on NYS-LAMS-only: the protocol names Cincinnati as the required scale, with regional scales in addition. Documenting NYS-LAMS alone still captures the same three findings plus grip, so a reviewer gets everything Cincinnati asks, but if CPRPS QA ever asks "where's the Cincinnati," the answer is "contained within the NYS-LAMS components." Your call stands; just know the argument.
- Next: voice-consistency pass, then the quick-reference shift version (skeletons only, notes stripped).

---

## 27a. ABBREVIATIONS

Abbreviations kept in the standard's emitted text, for a reader without EMS background. Field ids and internal identifiers are not covered here — they aren't printed.

- **NYS-LAMS** — New York State Los Angeles Motor Scale (prehospital stroke severity screen)
- **PMS** — pulse, movement, sensation
- **DCAP-BTLS** — deformities, contusions, abrasions, punctures/penetrations, burns, tenderness, lacerations, swelling
- **SLUDGE** — salivation, lacrimation, urination, defecation, GI upset, emesis (cholinergic toxidrome)
- **TECC** — Tactical Emergency Casualty Care
- **TOR** — termination of resuscitation
- **TQ** — tourniquet
- **ICS** — Incident Command System
- **RMA** — refusal of medical assistance
- **MOI** — mechanism of injury
- **LKW** — last known well
- **RED / YELLOW** — MCI triage categories (immediate / delayed)
- **START** — Simple Triage and Rapid Treatment (MCI triage method)
- **CCP** — casualty collection point
- **IC** — incident commander
- **MARCH** — massive hemorrhage, airway, respiration, circulation, hypothermia/head injury (trauma assessment sequence)
- **TXA** — tranexamic acid
- **TCP** — transcutaneous pacing
- **PEARL** — pupils equal and reactive to light
- **gtt** — drop/drip (IV flow rate)
- **OPQRST** — onset, provocation, quality, radiation, severity, time
- **NKDA** — no known drug allergies
- **ETCO2** — end-tidal carbon dioxide
- **GCS** — Glasgow Coma Scale
- **AMS** — altered mental status

---

## 28. REVISION HISTORY

**v0.10 — 2026-09-03.** Version roll-up of the worksheet-fix pass (builder PRs #16–#20): nothing is written until the medic accepts it; sentences, fields, and blocks can be deleted and restored; grouped rows indent under their first row; twin sentences across stacked blocks are stated once; each block or template prints as its own paragraph; GCS, NYS-LAMS, and burn % BSA are scored components with computed totals; 26 abbreviations spelled out and canonical forms fixed. The dated v0.10 entries below record each ruling. Builder tag and DOC meta read v0.10.

**v0.10 — 2026-09-02.** Block-per-paragraph. The narrative is no longer four paragraphs with every block crowded into the third: the four shell paragraphs stay fixed, and each stacked block or template now prints as its own paragraph between the assessment paragraph and the disposition paragraph, in the order the blocks were stacked. Conventions (§Conventions) and the §1 [BLOCK SLOT] note restated accordingly — the slot marks where block content is authored, not where it prints, so the assessment paragraph now ends with Secondary and the blocks follow it. Worked sample (§26) respaced: the assessment paragraph now ends with Secondary, and the Cardiac block follows it as a paragraph of its own. Paragraph identity in the builder becomes a token rather than a number (`p1`–`p4` for the shell, the owner id for a box), so a sentence or box moved into a block's paragraph stays with that block; the `¶N` badge shows the printed position, and a box — being a paragraph itself — never adopts one when dragged. No version bump: nothing clinical changed.

**v0.9 — 2026-09-01.** Sync pass closing the SYNC DEBT between this MD and the builder's DOC (18 defaults-review changes had been applied to the DOC directly, MD trailing until now — 13 of them needed MD-side sync, listed below), plus three demotion rulings from the same review.
- Meds marked multi-select (`{any that apply}`).
- LOC moved to the shell A&Ox/mental-status sentence with full capture — `[+ LOC ~___ min / - LOC / unknown LOC]`, unconditional for every call type; the traumaGeneral MOI's own `LOC [Y ___ min / N / unknown]` line removed as redundant.
- DCAP-BTLS pill added ahead of the traumaGeneral injuries line.
- Posturing options: `[none / decorticate / decerebrate]`.
- Basilar skull fx signs: named multi-select options (fluid from L/R ear, halo sign, Battle sign, raccoon eyes; none exclusive by convention).
- Hemorrhage control reassessment: "holding" → "bleeding controlled".
- Abdominal exam: "rebound" → "rebound tenderness".
- Pupils: "equal" → "PEARL".
- Terminology: "CMS" → "PMS" (pulse, movement, sensation) at all 7 distal/splint/restraint sites; underlying field ids unchanged.
- Spinal motion restriction moved from Trauma General to the shell Primary line, conditional on traumaGeneral/traumaMinor/burns (Trauma Major keeps its own spinal motion restriction line in §6); Trauma Minor now cross-references the shell line instead of carrying none.
- Seizure duration: free-text minutes → `[<5 min / >5 min, ~___ min / status epilepticus]` pill.
- Seizure line reordered: witnessed, type, pattern, then duration.
- Ruling A (abdominal last oral intake): the block owns it — Abdominal's own last-oral-intake line stays, the shell's last oral intake line no longer auto-expands for abdominal (builder-side condition change; cardiac/metabolic unaffected).
- Ruling B (ACS serial 12-lead): demoted to optional, styled `{If performed:}` after the §2a Symptomatic HTN/Hypotension precedent.
- Ruling C (dysrhythmia pads): split out of the IV line into its own optional `{If performed:}` line; emitted wording unchanged when filled.
- Conventions: added the multi-select notation (`{any that apply}`, applied here and to the five pre-existing multi fields already in the doc) and the four-paragraph structure statement.
- Worked sample (§26): respaced to the four-paragraph model, A&Ox sentence updated to a real emission (`A, - LOC,`), meds sentence simplified to "Meds per list, compliant.", Associated list made a valid Oxford emission ("diaphoresis, N/V, and lightheadedness").

**v0.9 addendum — 2026-09-01.** Chronology ruling: paragraph membership and within-paragraph order are defaults the author may rearrange to match the actual flow of the call (Conventions updated). Builder v1 implements it as drag-and-drop — a grab handle on every sentence and block, per-call arrangement saved with the draft, ¶ badges marking anything moved out of its home paragraph, and a Reset order control restoring the defaults. Block-internal reordering follows the same principle the MARCH note in §6 already states: the narrative reads in the order you did it.

**v0.10 — 2026-09-02.** Twin-sentence ruling: two stacked blocks (or two arms of one fork) can each carry a sentence that says the same thing — analgesia withheld, a 12-lead, IV access, GCS restated after an escalation, an NS bolus, an epi infusion. Rather than print it twice, the first block in the chart states it and later blocks' copies are hidden by default, restorable by the medic if the finding actually differs call to call (Conventions updated). The builder's DOC carries the twin groups as `meta.twins`, keyed by the underlying line ids so the engine can suppress a later block's duplicate render. Grouping was done two ways: identical rendered skeletons (fills/choices replaced with a placeholder) across different blocks/templates, and fields joined by an existing escalation `carry` map (e.g. Trauma General's GCS carrying into Trauma Major's). Twenty-two groups identified this pass (all IV-access sentences form one group, as do all initial 12-lead sentences); two block-internal candidates (CPAP withheld in the Respiratory fork, sedation matched only by its withheld wording in Tox) were checked and excluded — the first because its fork can render only one arm at a time, the second because the matching skeleton was coincidental, not the same clinical sentence.

**v0.10 — 2026-09-02 (2).** Scored-field ruling: GCS (all three lines), NYS-LAMS, and burn % BSA are entered as their components — E/V/M, the four NYS-LAMS findings, and the rule-of-nines regions checked — with the builder computing and printing the total in the position the standard already prints it (Conventions updated). GCS's E/V/M and NYS-LAMS's droop/drift/grip become numbered-pill choices; NYS-LAMS speech stays a plain finding, uncounted, matching the existing total of ___/6. The burns line is reworded to surface the % BSA computed from rule-of-nines regions ahead of the parenthetical instead of a free-text guess by palm method; first-degree exclusion moves from the line's note into a note on the new % BSA total. No wording the standard prints elsewhere changes, and no version bump.

**v0.10 — 2026-09-03.** Abbreviation spell-out pass: 26 abbreviations that weren't self-evident to an outside reader were spelled out in full wherever they appear in emitted text, hints, labels, and notes (LMP, EBL, non-tender for NT, bilaterally for bilat, private medical doctor for PMD, postpartum hemorrhage for PPH, spinal motion restriction for SMR, creatine kinase-relevant, paroxysmal nocturnal dyspnea for PND, packs per day for ppd, phosphodiesterase-5 inhibitor for PDE-5, diabetes mellitus / type 2 diabetes mellitus for DM/DM2, Comprehensive Psychiatric Emergency Program-capable for CPEP-capable, Director of Community Services for DCS, Mental Hygiene Law for MHL, gestational diabetes mellitus for GDM, hyperlipidemia for HLD, last known alive for LKA, musculoskeletal for MSK, rupture of membranes for ROM, skin / mucous membranes for Skin/MM, disorder for d/o, suicidal / homicidal ideation for the SI/HI pairing, and last oral intake for LOI in this section). Behavioral "HI" alone now reads "homicidal ideation" ("SI" stands alone, unchanged); the glucometer over-range option ("BGL ___ [HI]") now reads "BGL ___ [High (over range)]". Four terms were canonicalized to one spelling throughout: LAMS/S-LAMS/NY S-LAMS → NYS-LAMS; lower-case standalone "hx" → "Hx" (PMHx/FHx untouched); "A+Ox"/"AOx" → "A&Ox"; "MOLST/DNR" → "DNR/MOLST"; NYP-Hudson Valley → NYP-HVHC. "II" (Mobitz type II, Level I/II trauma center) and "CMS"/"PMS" needed no change — already in full or already correct per the prior ruling. New §27a Abbreviations appendix added, listing ~25 abbreviations kept as-is with one-line expansions. No wording change beyond these substitutions; no version bump.

**v0.11 — 2026-09-06.** Field Ledger review applied (first pass: shell, cardiac, active shooter, dispositions). 57 blanks removed, almost all intervention timestamps that already live in the emsCharts activity log; with them went three payload-only clauses (ACS suspected etiology, ACS IV fluids/bolus, lidocaine dose). One line removed: last menstrual period. Option lists tightened on 12 choices: "concerning for" → "unstable", "UNSTABLE" → "unstable", "focused" → "focused exam", "head-to-toe" → "head-to-toe exam", "repeated" → "unconverted"; dropped "refuses" (bare), "rate change", "Pt contact made", "warm zone established at ___". Seven fields changed control (free text ↔ pills/chips): card_acs_riskfactors, sh_lung_sounds, sh_pulse_status, sh_molst_detail, card_brady_tcp_confirm, card_narrow_irreg_drug, card_wide_stable_drug. "other…" escape toggled on 26 choices; 7 hints rewritten to Alex's wording. Worksheet-only: question-style labels on 20 fields (`q` property, narrative unaffected) and 22 pre-selected defaults. Version bump to v0.11: structural DOC change.

**v0.12 — 2026-09-06.** Clock-time inputs removed across every remaining category and template: 259 blanks deleted (ids ending `_time`, `_t1`–`_t5`, `_time_val`, and the unmasked epi/defib/ROSC/STEMI-identified/call-time stamps), all timestamps of EMS actions or observations that already live in the emsCharts activity log. Kept: history facts reported by others (last known well, symptom onset, time of injury, exposure time, witnessed-arrest time, "found at," "last seen at baseline," pre-EMS epi-pen/antipyretic use) and durations/intervals (q___ min, ___ min apart, downtime, submersion minutes, LOC minutes, APGAR 1/5). Sentences tidied by dropping the "at ___" phrase; a line whose only blank was the time stays as a fixed sentence (e.g. "ASA 324 mg chewed administered."). Seven lines hand-repaired after the automated pass: ca_tor_medcontrol, sh_medcontrol_line, ob_pph, ob_delivery, doa_found, brn_dressings, brn_eye. 67 option labels regenerated across 47 lines; 6 stale carry entries removed. Builder: HHMM mask and soft clock validation removed. Version bump to v0.12: structural DOC change.