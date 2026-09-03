# PCR Narrative Standard, Draft v0.10
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
35M___ dispatched to ___ for ___. 35M___ responded [emergency / non-emergency]. 35M___ arrived on scene (___ on location) and found ___ yo [M/F] pt ___ {position, location, appearance, scene}.

**Primary**
{traumaGeneral / traumaMinor / burns only — traumaMajor uses its own spinal motion restriction line in §6:} Spinal motion restriction: [c-collar applied and secured to stretcher at ___ for ___ {AMS or intoxication, neck/spine pain or tenderness, weakness/tingling/numbness since injury, spinal deformity, distracting injury, high-risk MOI: axial load, high-speed MVC/rollover, ped or bike struck, fall >3 ft/5 steps/pt height, or Red criteria blunt} / not indicated: no AMS, no spine pain or tenderness, no neuro sx, no deformity, no distracting injury, MOI not high-risk {use caution >65}].
Pt [+/-] patent airway, [+/-] breathing w/ initial L/S ___, [+/-] ___ pulse {location, quality}, skin ___.
{Conditional line, only if something was done before the full assessment:} ___ {e.g. "Pt placed on NRB 15 LPM." "Narcan 4 mg IN administered." "Tourniquet applied R thigh ___." Delete if nothing.}

**Mental status / CC / History**
Pt A&Ox___ (P, P, T, E), [A/V/P/U], [+ LOC ~___ min / - LOC / unknown LOC], and complaining of ___ {onset, duration, in pt's words}. [Pt / bystanders / family / healthcare staff] state ___.
Pt PMHx ___. Meds [per list / ___ / noncompliant ___] {any that apply}. Allergies [NKDA / ___]. {Add: last oral intake, last menstrual period, DNR/MOLST status when relevant.}

**Assessment**
Vitals as noted in emsCharts activity log, [stable / concerning for ___] {restate only the numbers that drive the DDx or a treatment}.
Working impression ___. DDx ___.

**[BLOCK SLOT]**
{Where the call-type blocks and templates are authored — treatments, withheld treatments with reason, reassessment, escalation line. This marks authoring position, not print position: each stacked block or template prints as its own paragraph AFTER the assessment paragraph (impression, then Secondary below) and before the disposition paragraph, in the order they were stacked.}

**Secondary**
Secondary assessment [head-to-toe / focused ___] unremarkable except ___.

**Ongoing / Medical control**
Pt reassessed en route at ___: ___ {the load-bearing change: pain 7 to 3, SpO2 88 to 96, rhythm unchanged}. Remaining vitals per activity log.
{Delete if none:} Medical control contacted at ___, Dr. ___ at ___, orders received for ___. {Any protocol deviation named here, plainly.}

**Disposition (pick one)**

*1) ALS transport*
Pt txp ALS to ___. Hospital notified via [cell / radio] at ___. [No pt changes throughout txp / ___]. Pt transferred to ED staff, report given to RN ___. 35M___ returned to service without further incident.

*2) Transport BLS*
Pt assessed, no ALS intervention indicated: ___ {the reason in one clause: 12-lead no acute changes, vitals stable, BGL normal, pain controlled}. Pt released to ___ {agency} BLS crew for txp to ___, report given to EMT ___. Pt [stable / unchanged] at time of release. 35M___ returned to service without further incident.

*3) 35M# cancelled*
35M___ cancelled [en route / on scene] by ___ {agency, unit, dispatch} at ___ for ___ {no pt found, pt refused prior to arrival, BLS handling, duplicate call}. [No pt contact made. / Pt contact made, ___ {brief assessment if any}.] 35M___ returned to service without further incident.

*4) RMA by 35M#*
Pt [refuses transport / refuses assessment / refuses ___] against medical advice. Pt A&Ox4, gait ___, [no evidence of AMS, intoxication, head injury, suicidal intent, or irrational behavior / ___], demonstrates capacity by restating in own words the nature of the complaint and the consequences of refusing. Transport to hospital offered. Pt advised that refusing may increase the possibility of serious illness, permanent disability, and death, including ___ {the worst plausible outcome for this complaint}. Pt advised to seek medical attention, follow-up instructions given: ___. Pt confirmed understanding and continues to refuse. Pt advised to call 911 with any return or worsening of symptoms. High-risk refusal [N / Y: ___ {>65, HR >120 or <50, SBP >200 or <90, RR >29 or <10, CP/SOB/syncope/focal deficit, significant MOI, ALS meds given}, medical control contacted, see above]. RMA signed by pt, witnessed by ___ {PD, family, partner}. Pt left in care of [responsible adult ___ / self]. 35M___ returned to service without further incident.

---

## 2. CARDIAC BLOCK
Categories: Cardiac Related Problem, Chest Pain, Heart Problems, Hypertension (symptomatic), Hypotension
Two sub-blocks. Chest pain with a normal rhythm uses 2a only. A rhythm problem without chest pain uses 2b only. Both when both.
Escalates to: STEMI template (2a). Cardiac Arrest template if pulses lost (2b). Hypotension with a shock picture: name the etiology in DDx and add the matching block (Tox, Sepsis, Trauma, Allergic).

### 2a. Cardiac / ACS
Pt describes ___ {OPQRST: onset, provocation, quality, radiation, severity ___/10, time, exertional or at rest, prior similar}. Associated [SOB / diaphoresis / N/V / lightheadedness / syncope / palpitations / none] {any that apply}. Cardiac risk factors ___ {HTN, hyperlipidemia, diabetes mellitus, smoker, FHx, prior MI/CABG/stent, cocaine use}.
12-lead acquired at ___ {before NTG if pt has no Rx NTG}: ___ {rhythm, rate, axis, intervals, ST/T changes by lead, or "no acute changes"}, transmitted at ___. {If inferior changes: R-sided 12-lead ___. If STE: jump to escalation line.}
ASA 324 mg chewed [administered at ___ / withheld: ___ {allergy, unable to chew, active GI bleed}]. {Took ASA before arrival but dose uncertain: give and say why.}
NTG 0.4 mg SL [x___ at ___, ___ min apart, SBP ___ before each dose, pain ___ to ___/10 / withheld: ___ {SBP ≤120 or MAP ≤90, R-sided changes, phosphodiesterase-5 inhibitor within 48h}]. {SBP drops <100 after NTG: supine, NS 500 mL bolus at ___, reassessed ___.}
IV ___g ___ at ___ {or IO, or attempts failed x___}. Fluids [none / ___ mL NS bolus for SBP ___, reassessed ___].
Fentanyl ___ mcg [IV / IM / IN] at ___ {1-1.5 mcg/kg, repeat after 10 min, max 200 mcg total} for pain ___/10 unrelieved by NTG, pain ___ to ___/10 / withheld: ___ {pain improved, pt declined, SBP, AMS}. {No ketorolac in suspected ACS.}
{Symptomatic HTN only:} BP ___ with ___ {headache, vision change, CP, neuro deficit}. Neuro exam ___. No antihypertensive given.
{Hypotension only:} SBP ___, ___ {skin, mental status, cap refill}. Suspected etiology ___. ___ mL NS bolus at ___, reassessed SBP ___. {Pressor only w/ med control, cite in Medical control line.}
{If performed:} Serial 12-lead at ___: [unchanged / ___].
**Escalation line:** STEMI criteria [not met on serial 12-leads / MET: ___ {leads, mm}, STEMI alert called to ___ at ___, 12-lead transmitted. Switch to STEMI template.]

### 2b. Cardiac / Dysrhythmia
Monitor at ___: ___ {rhythm, rate, regularity, QRS width, P-wave relationship, block degree and type}. 12-lead at ___ confirms ___. {Print and attach the strip that shows the diagnosis.}
Pt [hemodynamically stable / UNSTABLE: ___ {which of: SBP <90, AMS, ischemic CP, acute CHF, syncope}]. Onset ___ {known time, or "unknown, >48h" for rate-control decisions}. Prior Hx of this rhythm [Y, ___ / N]. Anticoagulated [Y ___ / N].
IV ___g ___ at ___.
{If performed:} Pads applied at ___ [prophylactically / for pacing / for cardioversion].

{Pick the fork that applies. Delete the rest.}

*Bradycardia:*
Atropine 1 mg IV at ___ {q3 min, max 3 mg}, x___, HR ___ to ___, [symptoms resolved / no response] / withheld: ___ {asymptomatic, 2nd-degree type II or 3rd-degree block with poor perfusion went straight to pacing, transplant}.
TCP initiated at ___, rate ___, capture at ___ mA confirmed by [pulse / SpO2 pleth / ___]. Sedation: midazolam [2.5 mg IV / 5 mg IM] at ___ {repeat q5 if SBP >100 or MAP >65} / withheld: ___ {SBP, AMS}.
Epi infusion started at ___ mcg/min at ___ {start 5 mcg/min, titrate to MAP >65 or SBP >100}, titrated to ___ mcg/min, MAP ___ to ___ / not indicated: ___.

*Narrow-complex tachycardia:*
{Stable, REGULAR:} Vagal maneuver at ___ [modified Valsalva / ___ (no carotid massage)], [converted / no change]. Adenosine 6 mg rapid IV with flush at ___, [converted to ___ at ___ / no change / transient block revealing ___]. Adenosine 12 mg at ___, ___.
{Stable, IRREGULAR:} Diltiazem ___ mg IV over 2 min at ___ {0.25 mg/kg, max 25 mg} for ___ {A-fib/flutter RVR}, HR ___ to ___, BP ___ to ___ / metoprolol 5 mg IV over 2 min at ___ (pt on Rx beta-blocker) / withheld: ___ {SBP, WPW, CHF}. {Uncontrolled after 15 min or recurrent:} Diltiazem ___ mg at ___ {0.35 mg/kg, max 35 mg} / second metoprolol 5 mg at ___.
{UNSTABLE, regular or irregular:} Sedation [midazolam 2.5 mg IV / 5 mg IM] ___ at ___ / withheld: ___ {SBP, AMS, time-critical}. Synchronized cardioversion 200 J at ___, [converted to ___ / repeated at ___ J at ___]. Pt [aware / not aware] during shock. 12-lead post-conversion at ___.

*Wide-complex tachycardia:*
QRS ___ ms. Treated as VT [stable / UNSTABLE].
{Stable:} Amiodarone 150 mg in 100 mL NS over 10 min at ___ / lidocaine ___ mg IV at ___ {1.5 mg/kg}, [converted at ___ / rate ___ to ___ / no change] / withheld: ___ {unstable, went to cardioversion; polymorphic}.
{UNSTABLE:} Sedation [midazolam 2.5 mg IV / 5 mg IM] at ___ / withheld: ___. Synchronized cardioversion 100 J at ___ {200 J if irregularly irregular; max 3 attempts}, [converted to ___ / repeated ___ J at ___, ___ J at ___]. Antiarrhythmic post-conversion per med control: ___.
{Torsades / med control:} Mag 2 g IV over [10 min stable / 2 min unstable] at ___ per Dr. ___.

Post-intervention rhythm ___ at ___, 12-lead at ___: ___. Pt [symptoms resolved / ___].
**Escalation line:** Pt remained [hemodynamically stable / stable after intervention] throughout / became unstable at ___, ___ {intervention}. Pulses [maintained throughout / LOST at ___. Switch to Cardiac Arrest template.]

---

## 3. RESPIRATORY BLOCK
Categories: Breathing Problems, Choking, COVID-19 Related/Potential
Escalates to: Respiratory Arrest template. Allergic block if anaphylaxis is the cause. Cardiac block if CHF from a rhythm or ACS.

Pt [speaking full sentences / ___-word sentences / unable to speak], [tripod / supine / ___], accessory muscle use [Y / N], [retractions / nasal flaring / pursed lips / none] {any that apply}. RR ___, SpO2 ___% on [RA / ___]. L/S ___ {by field: clear, wheezes, rales, rhonchi, diminished, absent}, ETCO2 ___ with [normal / shark-fin / ___] waveform.
Onset ___ {sudden / gradual over ___}, [exertional / at rest], associated [fever / productive cough ___ / CP / orthopnea / paroxysmal nocturnal dyspnea / leg swelling / recent illness / sick contacts / travel / none]. Hx [asthma / COPD / CHF / PE / smoker ___ packs per day / home O2 ___ LPM / prior intubation for this]. Rescue inhaler used ___ times prior to arrival.
Working etiology ___ {reactive airway, CHF/pulmonary edema, pneumonia, PE, pneumothorax, FBAO, other}.

O2 via [NC / NRB / BVM] ___ LPM at ___, SpO2 ___ to ___.
{Pick the fork that applies. Delete the rest.}

*Reactive airway (asthma / COPD):*
Albuterol 2.5 mg / ipratropium 0.5 mg neb at ___, repeated at ___, ___ {max 3 albuterol on standing order}, L/S ___ to ___, RR ___ to ___ / withheld: ___.
Dexamethasone 10 mg [IV / IM / PO] at ___ / withheld: ___.
Mag 2 g in 100 mL NS IV over 10 min at ___ for asthma not responding to above / withheld: ___. {COPD: med control only, cite.}
Epi 0.3 mg (1 mg/mL) IM at ___ for severe distress {tidal volume too small for neb}, repeated at ___ {q5 if persists} / withheld: ___.
CPAP ___ cmH2O at ___ {5-10}, tolerated [well / ___], SpO2 ___ to ___ / withheld: ___ {AMS, vomiting, SBP, unable to protect airway}.

*CHF / pulmonary edema:*
CPAP ___ cmH2O at ___ {5-10}, tolerated [well / ___], SpO2 ___ to ___, RR ___ to ___ / withheld: ___ {SBP, AMS, vomiting, facial trauma}.
NTG 0.4 mg SL [x1 / x2 / x3] at ___ per SBP ___ {SBP 120-160: 1 tab q5; 160-200: 2 tabs q5; >200: 3 tabs q5}, repeated at ___, BP ___ to ___ / withheld: ___ {SBP <120, phosphodiesterase-5 inhibitor}.
12-lead at ___: ___ {rhythm, ischemic changes}. {If ACS suspected, add 2a.}

*FBAO (Choking):*
[Partial / complete] obstruction, pt [coughing effectively / unable to cough or speak / unresponsive] on arrival. Abdominal thrusts x___ by [bystander / crew] at ___. Laryngoscopy at ___, ___ {object seen or not}, removed with Magill forceps at ___ / not visualized. Airway [patent after removal / ___]. Post-event L/S ___, SpO2 ___.

*Pneumonia / infectious / COVID:*
Temp ___, [sepsis screen: see Metabolic/Sepsis block if positive]. Isolation precautions ___. Supportive O2 as above.

*Suspected pneumothorax:*
L/S [absent / diminished] ___ side, [tracheal deviation / JVD / subcutaneous emphysema / none]. {Tension with hemodynamic compromise:} Needle decompression ___ side, ___ ICS ___ line, at ___, [rush of air / improvement in ___] / not indicated: ___.

Pt reassessed at ___: [work of breathing improved / unchanged / worsening], RR ___, SpO2 ___, ETCO2 ___, L/S ___.
**Escalation line:** Pt [maintained adequate spontaneous respirations throughout / respirations became inadequate at ___, BVM initiated. Switch to Respiratory Arrest template.]

---

## 4. NEURO / AMS BLOCK
Categories: Altered Mental Status, Dizziness, Headache, Seizure, Syncope (near), Syncope/Fainting, Unconscious/Unresponsive
Escalates to: Stroke/CVA template. Tox block if overdose is the cause. Metabolic block if hypoglycemia or sepsis is the cause and corrected. OB block for seizure in pregnancy or ≤6 wks postpartum.

GCS ___ (E___ V___ M___), pupils ___ {size, equality, reactivity}. Baseline mental status per [family / facility / ___]: ___. Last known well ___ {time and source}.
BGL ___ at ___. Temp ___. {SpO2 and ETCO2 per activity log unless abnormal: ___.}
NYS-LAMS: facial droop [absent 0 / present 1], arm drift [absent 0 / drifts 1 / falls rapidly 2], speech [normal 0 / abnormal 1], grip [normal 0 / weak 1 / none 2], total ___/6. [Negative, no deficits / POSITIVE ___, see escalation line].
Onset ___ {sudden / gradual}, [witnessed by ___ / unwitnessed, found at ___]. Associated ___ {headache, worst-ever, neck stiffness, fever, trauma, incontinence, tongue biting, recent illness, new meds, missed meds, ETOH/drug use}. Hx ___ {seizure disorder, prior CVA, dementia, diabetes mellitus, psych, ETOH}. Anticoagulated [Y ___ / N].

{Pick the fork that applies. Delete the rest.}

*Seizure:*
Seizure [witnessed by ___ / reported], type ___ {generalized tonic-clonic, focal, absence}, [single / x___ / continuous on arrival], [<5 min / >5 min, ~___ min / status epilepticus]. Postictal on arrival [Y, GCS ___ / N]. Seizure Hx [Y, typical for pt / Y, atypical: ___ / N, first-time]. Meds [compliant / missed ___]. Injuries from seizure ___.
Midazolam [10 mg IM / 10 mg IN / 5 mg IV] at ___ for [active seizure / recurrent without return to baseline], seizure [stopped at ___ / continued, repeat dose ___ at ___ {once, after 5 min}] / withheld: ___ {self-terminated, postictal only}. {Pregnant or ≤6 wks postpartum: OB block, mag per pre-eclampsia/eclampsia protocol.}
Recovery: GCS ___ to ___ by ___.

*Syncope / near-syncope:*
Event [witnessed / unwitnessed], [prodrome ___ / none], duration of LOC ___, [return to baseline / persistent ___]. Position at onset ___ {standing, seated, exertional, straining}. 12-lead at ___: ___ {rhythm, intervals, blocks, WPW, Brugada, prolonged QT, or "no acute changes"}. Orthostatics [___ supine to ___ standing / not obtained: ___]. Injuries from fall ___. {Exertional, cardiac Hx, abnormal 12-lead, or age >65: name it as the reason for ALS.}

*AMS / unresponsive:*
Hypoglycemia [ruled out, BGL ___ / treated, see Metabolic block]. Opioid toxidrome [absent / present: ___, see Tox block]. Naloxone ___ mg [IN / IM / IV] at ___ for RR ___ {only for respiratory insufficiency}, response ___ / withheld: ___ {respirations adequate}. Airway [self-maintained / NPA / OPA / positioned]. Trauma [none evident / ___, see Trauma block]. Sepsis screen [negative / positive, see Metabolic block]. Post-ictal state [considered / ___]. 12-lead at ___: ___. {If none of the above explains it, say so: "no reversible cause identified in the field."}

*Headache / dizziness:*
Headache: onset ___, [thunderclap / gradual], severity ___/10, [worst of life Y/N], with [visual change / neck stiffness / fever / neuro deficit / none]. BP ___.
Dizziness: [vertigo (spinning) / lightheadedness / disequilibrium], [positional / constant], with [nystagmus / ataxia / dysmetria / diplopia / dysarthria / none] {any of these with a normal stroke screen still gets "posterior circulation not excluded" in DDx}.

IV ___g ___ at ___. Treatments per fork above. Pt reassessed at ___: GCS ___, NYS-LAMS [unchanged ___ / ___].
**Escalation line:** Stroke screen [negative on initial and reassessment, no focal deficit, LKW ___ / POSITIVE, NYS-LAMS ___/6, LKW ___ per ___, stroke alert called to ___ at ___. NYS-LAMS 0-3: NYS-designated stroke center ___. NYS-LAMS 4-6: exclusion criteria reviewed ___, routed to thrombectomy-capable center ___. SBP maintained >120 / SBP ___ >220, med control contacted. Switch to Stroke/CVA template.]

---

## 5. TRAUMA GENERAL BLOCK
Categories: Assault, Fall Victim, Industrial Accident, Pain (Traumatic), Traffic Accident
Escalates to: Trauma Major block on any RED criterion, or a discretionary trauma alert. YELLOW criteria alone: pt goes to a trauma center, documented here, block stays General. Cardiac Arrest template (trauma addendum) if pulses lost.

MOI: ___ {fall from ___ ft onto ___, MVC ___ mph, restrained/unrestrained, airbag, intrusion ___, ejection, rollover, windshield/steering wheel deformity, assault with ___ to ___, machinery ___}. Time of injury ___. [Helmet / seatbelt / PPE] {any that apply} [Y / N / unknown]. Ambulatory on scene [Y / N]. {Elderly, anticoagulated, or intoxicated: say so here, it changes the triage math.}
GCS ___ (E___ V___ M___), pupils ___. Pt [denies / reports] head, neck, or back pain. Distracting injury [Y ___ / N]. Intoxication [Y / N].
[no DCAP-BTLS observed head-to-toe / DCAP-BTLS +]. Injuries found on exam: ___ {by region, head to toe, with side. "Contusion L lateral chest wall, no crepitus, no paradoxical movement." Or "No injuries found."} Distal PMS [intact x4 / ___].
Hemorrhage control: [none required / direct pressure ___ at ___ / pressure dressing / hemostatic gauze packed ___, pressure held ___ min / tourniquet ___ 2-3 in proximal at ___, time written on TQ, second TQ at ___]. TQ conversion [not attempted / attempted at ___: pressure dressing applied, windlass released, ___ {no rebleed, TQ left in place loose / rebleed, re-tightened}]. Estimated blood loss ___.
Splinting: ___ {what, how, PMS before and after} / not indicated.
Analgesia {one narcotic on standing order}: fentanyl ___ mcg [IV / IM / IN] at ___ {1-1.5 mcg/kg, repeat after 10 min, max 200 mcg} / morphine ___ mg at ___ / ketamine [25 mg IV over 5 min / 50 mg IM] at ___ / acetaminophen 1000 mg PO at ___ {not if >650 mg within 4h, liver dz, shock} / ketorolac 15 mg [IV / IM] at ___ {not if >60, anticoagulated, bleeding, renal, pregnant}, pain ___/10 to ___/10 / withheld: ___ {pain controlled, SBP, AMS, pt declined}.
IV ___g ___ at ___. Fluids [none / ___ mL NS for SBP ___, reassessed ___].
Field triage criteria reviewed at ___: RED [none / ___]. YELLOW [none / ___ {high-risk auto crash: ejection, intrusion >12 in occupant or >18 in any site, extrication, death in compartment, telemetry; rider separated with significant impact; ped/bike thrown or run over; fall >10 ft; EMS judgment: low-level fall ≥65 or ≤5 with head impact, anticoagulant use, pregnancy >20 wks, burns with trauma}].
**Escalation line:** [No RED or YELLOW criteria, trauma alert not indicated, txp to ___ / YELLOW criteria only (___), txp to trauma center ___ / RED criterion MET: ___, switch to Trauma Major block.] {Discretionary: "Trauma alert called at provider discretion for ___."}

---

## 6. TRAUMA MAJOR BLOCK
Categories: Head Injury, Stab/Gunshot Wound, Traumatic Injury, Hanging/Strangulation/Asphyxiation, plus anything from Trauma General meeting a RED criterion or getting a discretionary alert
Escalates to: Cardiac Arrest template with trauma addendum if pulses lost. Neuro block does not apply; head injury findings live here.
{Order matters in this block: it reads as the MARCH sequence because that's the order you did it in.}

MOI: ___ {as Trauma General, plus for penetrating: weapon, number of wounds, entrance/exit if known; for hanging: ligature type, suspension time, drop height, who cut down}. Time of injury ___. LOC [Y ___ min / N / unknown].
RED criteria MET: ___ {name them: penetrating head/neck/torso/proximal extremity; skull deformity or suspected fx; spinal injury with new motor/sensory loss; chest wall instability or flail; suspected pelvic fx; 2+ proximal long bone fx; crushed/degloved/mangled/pulseless extremity; amputation proximal to wrist/ankle; bleeding requiring TQ or packing with continuous pressure; motor GCS <6; RR <10 or >29 or respiratory support; RA SpO2 <90%; SBP <90 (10-64 yo) or <110 (≥65) or HR > SBP; or provider discretion ___}. Trauma alert called to ___ at ___. Destination: highest-level trauma center available: ___.
GCS ___ (E___ V___ M___) at ___, pupils ___. {Head injury: repeat GCS at ___ and ___; any drop of 2 or more gets its own sentence with the time.}

Massive hemorrhage: [none / ___ {site}, controlled with ___ {TQ at ___ with time on TQ, wound packing, pressure dressing, junctional}, estimated blood loss ___].
Airway: [patent, self-maintained / ___ {NPA, OPA, suction for ___, positioned}]. {Advanced airway: device, size, attempts, confirmation by ETCO2 ___ and ___, secured at ___ cm, time.}
Respirations: L/S ___ bilaterally, chest [symmetric / ___ {paradoxical, crepitus, open wound}]. Occlusive dressing to ___ at ___. Needle decompression ___ side, ___ ICS ___ line at ___, [rush of air / SBP ___ to ___] / not indicated: ___. SpO2 ___, ETCO2 ___.
Circulation: radial pulse [present / absent], SBP ___, MAP ___, skin ___. IV/IO ___g ___ at ___, second access ___. NS 500 mL bolus at ___ for SBP <100 / MAP <65, reassessed SBP ___, L/S ___, repeated ___ {to 2 L max while L/S clear, goal SBP ≥100 / MAP ≥65}. TXA 2 g in 100 mL over 10 min at ___ for traumatic hemorrhage with SBP <100 / withheld: ___ {SBP ≥100}. Pelvic binder at ___ for ___ / not indicated.
Head/spine: spinal motion restriction via ___ at ___. Pupils ___, [PEARL / unequal ___], posturing [none / decorticate / decerebrate]. Signs of basilar skull fx [none / fluid from L ear / fluid from R ear / halo sign / Battle sign / raccoon eyes] {any that apply; none is exclusive by convention}. Anticoagulated [Y ___ / N]. {Herniation signs: hyperventilation to ETCO2 ___ at ___, or say not indicated.}
Hypothermia prevention: ___ {blankets, heat on, wet clothing removed}.
Injuries found on exam: ___ {head to toe, by region, with side}. Distal PMS ___.
{Hanging/strangulation add:} Ligature marks ___, petechiae [face / conjunctiva / none], voice change [Y / N], stridor [Y / N], subcutaneous emphysema [Y / N]. C-spine ___. {Airway swelling is delayed; say you reassessed it.}
Splinting ___. Analgesia: fentanyl ___ mcg ___ at ___ / ketamine ___ mg ___ at ___, pain ___ to ___ / withheld: ___ {SBP, GCS, airway}.
Pt reassessed at ___: GCS ___, SBP ___, SpO2 ___, ETCO2 ___, hemorrhage control [bleeding controlled / ___].
Destination ___ {Level I / II trauma center, name}, [by ground / air, ___ requested at ___, landed ___]. Scene time ___ min {if >10 min, say why in one clause}.
**Escalation line:** Pulses [maintained throughout / LOST at ___. Switch to Cardiac Arrest template, trauma addendum.]

---

## 7. TOX BLOCK
Categories: Alcohol Related, CO Poisoning/Hazmat, Drug or Substance Use/Abuse, Ingestion/Poisoning, Overdose, Radiological Injury, Toxic Exposure
Escalates to: Respiratory Arrest or Cardiac Arrest template. Neuro block if AMS persists after reversal with no tox explanation. Behavioral block for intentional ingestion once medically stable.

Substance ___ {name, or "unknown"}, [ingested / injected / inhaled / dermal / ___], amount ___ {count, mL, bags}, time ___ {or "unknown, last seen normal ___"}, [intentional / accidental / recreational / unknown]. Co-ingestants [ETOH ___ / ___ / none reported]. Source of Hx [pt / bystander / pill bottles ___ {name, count remaining, fill date} / paraphernalia ___ / none]. {Bring the bottles.}
Toxidrome: [opioid: pinpoint pupils, RR ___, ___ / sympathomimetic: ___ / anticholinergic: ___ / sedative: ___ / cholinergic: ___ / none identified]. GCS ___, pupils ___, RR ___, SpO2 ___, ETCO2 ___, BGL ___, temp ___, skin ___.
12-lead at ___: ___ {QRS width, QTc, rhythm; say the number for TCA/sodium-channel and QT-prolonging agents}.
Airway [self-maintained / NPA / OPA / BVM at ___ for RR ___ or ETCO2 ___]. O2 ___.

{Pick the fork that applies. Delete the rest.}

*Opioid:*
Naloxone ___ mg [IN unit dose / IM / IV in ≤0.5 mg increments] at ___ by [bystander / PD / VAC / 35M___] for RR ___ {given only for respiratory insufficiency or arrest; max 2 mg/dose IV or IM, 4 mg IN}, response at ___: [RR ___ to ___, GCS ___ to ___ / no response, repeat dose ___ mg at ___] / withheld: ___ {respirations adequate, airway self-maintained}. Titrated to respiratory effort, not wakefulness. Not given after advanced airway placed. Pt [cooperative / agitated / withdrawal sx ___] after reversal. Pt advised naloxone wears off before ___; [accepts txp / see RMA].

*ETOH:*
Pt [ambulatory with assistance / unable to ambulate], speech ___, odor of ETOH [Y / N], last drink ___, [known ETOH Hx / withdrawal Hx / seizure Hx]. Head injury [none evident / see Trauma block]. BGL ___. {The chart has to show you looked for the thing that isn't ETOH: head injury, hypoglycemia, sepsis, stroke.}

*Sedative / unknown ingestion:*
Supportive care. Airway as above. Poison Control [contacted at ___, ref ___, recommendations ___ / not contacted: ___]. Activated charcoal [not given / ___ per med control].

*Sympathomimetic / agitated:*
Agitation: verbal de-escalation attempted ___ [effective / ineffective], environmental modification ___, danger to [self / crew / public]. BGL ___ when safe. Midazolam ___ mg [IM / IV] at ___ {up to 5, repeat to 10 total} / olanzapine [10 mg IM / 5 mg SL / 2.5-5 mg IM if ≥65] at ___ / ketamine 250 mg IM at ___ for ___ {clinical triad: psychomotor agitation, physiologic excitation, failed de-escalation, with ___ of: unusual strength, no tiring, pain tolerance, tachypnea, diaphoresis, hyperthermia, AMS}, repeated 250 mg IM at ___ {once, after 5 min} / withheld: ___. Response at ___: ___. Airway, SpO2, ETCO2 monitored continuously after sedation: ___. Temp ___ {hyperthermia treated with ___}. Restraints [none / soft, ___ points, applied at ___ by ___, supine, PMS checked q___, reason ___]. Pt not transported prone. PD [on scene / requested at ___].

*CO / hazmat / inhalation:*
Scene [safe / hazmat staged / ___ metered ___ ppm by ___]. Exposure duration ___, others exposed ___. SpCO ___ if available. High-flow O2 NRB 15 LPM at ___. Symptoms ___ {headache, N/V, confusion, syncope, CP}. Decon [performed by ___ / not required]. Destination [hyperbaric-capable ___ / ___].

*Cholinergic / organophosphate:*
SLUDGE findings ___. Decon at ___. Atropine ___ mg at ___, repeated ___, secretions [drying / ___]. DuoDote/pralidoxime ___ at ___ / not available.

*Radiological:*
Per hazmat/IC direction ___. Decon ___. Contamination survey ___. Treated as trauma/medical per presenting problem, see ___ block.

Pt reassessed at ___: GCS ___, RR ___, SpO2 ___, ETCO2 ___. Police [on scene / notified / not involved].
**Escalation line:** Pt [maintained adequate respirations and pulses throughout / respirations became inadequate at ___, BVM initiated, switch to Respiratory Arrest template / pulses lost at ___, switch to Cardiac Arrest template].

---

## 8. METABOLIC / SEPSIS BLOCK
Categories: Diabetic Problem, Fever/Sepsis
Escalates to: Neuro block if AMS persists after glucose corrected. Respiratory block if the source is pulmonary and needs its own treatment.

*Hypoglycemia:*
BGL ___ at ___. Pt [responsive, able to swallow / AMS, GCS ___ / unresponsive]. Last meal ___, last insulin/oral agent ___ {name, dose, time}, [usual regimen / recent change / missed meal / increased activity / ETOH]. Prior episodes [Y / N].
Oral glucose ___ g at ___ {15-30 g, able to swallow on command} / D10 ___ mL IV at ___ {up to 25 g / 250 mL} / glucagon 1 mg IM at ___ (IV unobtainable x___). Repeat BGL ___ at ___, GCS ___ to ___. D10 redosed ___ mL at ___ for recurrence / not required.
Pt [ate ___ after recovery / declined food]. Sulfonylurea or long-acting insulin on board [Y ___, recurrence risk explained / N]. {This line is what makes or breaks the RMA on a diabetic.}

*Hyperglycemia / DKA:*
BGL ___ [High (over range)]. Kussmaul respirations [Y / N], fruity odor [Y / N], polyuria/polydipsia ___ days, N/V ___, abd pain ___. Skin ___, mucous membranes ___. ETCO2 ___. 12-lead at ___: ___ {peaked T's, rhythm}. Insulin compliance ___, [pump: ___ / new dx]. IV ___g ___ at ___, NS ___ mL at ___, reassessed ___.

*Sepsis:*
Suspected source ___ {UTI, pneumonia, skin/wound, indwelling line/catheter, post-op, unknown}. Onset ___. Immunocompromised [Y ___ / N]. Facility/family reports ___.
Sepsis screen at ___: suspected infection [Y ___ / N] with [SBP <100 / AMS / neither]. Indicators: temp ___, HR ___, RR ___, ETCO2 ___, [fever, chills, diaphoresis, new cough, urinary sx, new AMS, flushed, pallor, rash, mottling]. [Meets septic shock criteria / suspected infection, criteria not met]. Skin ___, cap refill ___.
Large-bore IV ___g ___ at ___, second access ___. NS 500 mL bolus at ___ for SBP <100 / MAP <65, reassessed SBP ___ to ___, MAP ___, L/S ___ {repeat to 2 L while clear, goal SBP >100 / MAP >65; stop and say so if rales develop}, repeated at ___, ___. O2 NRB at ___. Hospital notified of suspected septic shock at ___ / not indicated: ___.
Norepi started at ___ mcg/min at ___ {2-20 mcg/min, after ≥1 L in, to MAP >65 / SBP >100}, titrated to ___, MAP ___ to ___ / not indicated: ___.

Pt reassessed at ___: BGL ___ / SBP ___, MAP ___, GCS ___.
**Escalation line:** [Hypoglycemia corrected, BGL ___, pt at baseline / BGL corrected but AMS persists, GCS ___, no other cause identified, see Neuro block] / [Sepsis screen negative / Sepsis screen POSITIVE, alert called, fluids as above].

---

## 9. GENERALIZED MEDICAL BLOCK
Categories: Abnormal Labs, General Illness/Malaise, Hypertension (a-symptomatic), Sick Person, Unable to Ambulate, Weakness, Fever/High Temperature
This is the block for "nothing specific." Its whole job is to prove the specific things were screened for and were negative. Escalates to whichever block the screen turns up.

Pt reports ___ {in their words: weak, tired, "not right," can't get up}, onset ___ {hours/days}, [gradual / sudden], [progressive / static]. Associated ___ {fever, chills, cough, dysuria, N/V/D, poor PO intake ___ days, falls, dizziness, CP, SOB, new meds, missed meds}. Last seen at baseline ___ per ___. Baseline function ___ {independent, walker, bed-bound}. Living situation ___ {alone, with family, facility}.
Screens at ___: BGL ___. Temp ___. Sepsis screen [negative / positive, see Metabolic block]. 12-lead [___ / not indicated: ___]. NYS-LAMS [0, no focal deficit / see Neuro block]. Orthostatics [___ / not obtained: ___]. Hydration: mucous membranes ___, skin turgor ___, urine output per pt ___.
{Fever/High Temp:} Temp ___, duration ___, [localizing sx ___ / none], sick contacts ___, antipyretics taken ___ at ___. Sepsis screen as above.
{Asymptomatic HTN:} BP ___ x___ readings, pt denies headache, vision change, CP, SOB, neuro sx. Neuro exam grossly intact. Med compliance ___. No treatment indicated; pt advised private medical doctor follow-up within ___.
{Abnormal labs:} Sent by ___ {private medical doctor, dialysis, facility} for ___ {lab, value, drawn ___}. Pt [symptomatic ___ / asymptomatic]. 12-lead at ___: ___ {mandatory for K, Ca, Mg, dig}. Treatment ___ / none indicated in the field.
{Unable to ambulate:} [Weakness / pain ___ / mechanical: ___]. Injuries [none / see Trauma block]. Lift assist only [Y, pt assessed and at baseline / N]. Skin check [intact / ___] if down time >1h. Creatine kinase-relevant down time ___.
IV ___g ___ at ___ / not indicated. Fluids ___ mL NS at ___ for ___ / none.
Working impression ___ {"generalized weakness, etiology unclear, dehydration vs UTI vs ___"}.
Pt reassessed at ___: ___.
**Escalation line:** Screens negative for hypoglycemia, sepsis, stroke, and acute cardiac cause; pt txp for ___ / [screen POSITIVE for ___, see ___ block].

---

## 10. ABDOMINAL / GI BLOCK
Categories: Abdominal Pain, GI Bleed, Nausea/Vomiting, Pain (Non-cardiac)
Escalates to: Metabolic/Sepsis block if septic; Cardiac 2a if epigastric pain is cardiac-suspicious (>35 yo, risk factors, diaphoresis); OB block if pregnant; Trauma if traumatic.

Pain: ___ {OPQRST, location by quadrant, radiation to back/groin/shoulder, quality}. Associated [N/V ___ episodes / diarrhea / constipation, last BM ___ / fever / urinary sx / melena / hematemesis ___ {coffee-ground, bright red, volume} / hematochezia / none] {any that apply}. Last oral intake ___. {Female of childbearing age: last menstrual period ___, pregnancy [possible / denied].}
Abd exam: [soft / rigid / guarded], [non-tender / tender ___ quadrant], [distended / non-distended], [rebound tenderness / none], [pulsatile mass / none]. {>50 with back/abd pain: bilateral femoral pulses ___, "AAA not excluded" in DDx if any asymmetry or hypotension.}
{GI bleed:} Skin ___, orthostatics ___, anticoagulated [Y ___ / N], prior GI bleed [Y / N], ETOH Hx [Y / N]. Estimated blood loss per pt/scene ___.
12-lead at ___ for epigastric/upper abd pain: ___ / not indicated: ___.
IV ___g ___ at ___. NS ___ mL at ___ for ___, reassessed ___ / none.
Ondansetron ___ mg [ODT / IV / IM] at ___ for ___ / isopropyl pad self-inhalation / withheld: ___.
Analgesia: fentanyl ___ mcg at ___, pain ___ to ___ / withheld: ___ {no ketorolac/ibuprofen for abd pain: bleeding risk}.
**Escalation line:** [No peritoneal signs, hemodynamically stable throughout / sepsis screen positive, see Metabolic block / hypotensive with GI bleed: ___ {fluids, goal}, hospital notified of unstable GI bleed at ___].

---

## 11. ALLERGIC BLOCK
Categories: Allergic Reaction
Escalates to: Respiratory Arrest template. Respiratory block for isolated bronchospasm without systemic signs.

Exposure: ___ {allergen, route, time}. Prior anaphylaxis Hx [Y, to ___ / N]. Epi auto-injector [used prior to arrival at ___ / prescribed, not used / none].
Presentation: [rash/hives ___ distribution / itching / facial or oral edema ___ / stridor / wheezing / resp distress / hypotension SBP ___ / GI sx: N/V, abd pain, diarrhea / ___]. [ANAPHYLAXIS: severe resp distress, facial/oral edema, or hypoperfusion, OR Hx of anaphylaxis + exposure + (resp distress / hypoperfusion / rash) / allergic reaction, systemic criteria not met].
Epi 0.3 mg (1 mg/mL) IM at ___, response at ___: ___, repeated at ___ {once, at 5 min if no improvement} / withheld: ___ {criteria not met}.
Albuterol 2.5 mg / ipratropium 0.5 mg neb at ___ for wheezing, x___ / withheld: ___.
IV ___g ___ at ___. NS 500 mL bolus at ___ for SBP <100 / MAP <65, reassessed ___, repeated ___ {to 2 L, L/S clear} / none.
Diphenhydramine 50 mg [IV / IM] at ___ / withheld: ___. Dexamethasone 10 mg [PO / IM / IV] at ___ / withheld: ___.
Epi infusion started at ___ mcg/min at ___ {start 5, titrate to MAP >65 / SBP >100}, titrated ___ / not indicated.
Pt reassessed at ___: airway ___, L/S ___, SBP ___, rash ___.
**Escalation line:** [Symptoms improving, airway patent throughout / airway compromise progressed at ___, ___. Switch to Respiratory Arrest template.] {Epi given + pt wants to refuse: med control per regional procedure, cite above.}

---

## 12. BEHAVIORAL BLOCK
Categories: Anxiety, Psychiatric Problems
Escalates to: Tox block for ingestion; Neuro block if medical cause suspected; the agitated-patient fork in Tox for chemical restraint (same documentation either way).

Presentation: ___ {in pt's words and observed affect/behavior}. [Danger to self: ___ / danger to others: ___ / neither expressed or observed] {any that apply}. SI [denied / expressed: ___ {plan, means}]. Homicidal ideation [denied / expressed: ___].
Medical screen: BGL ___, [no evidence of trauma, intoxication, hypoxia, or acute medical cause / ___]. Psych Hx ___ {dx, meds, compliance ___, prior admissions}. Recent stressors/changes ___.
De-escalation: [verbal effective, pt cooperative / ___]. PD [on scene / requested at ___ / not needed]. {Mental Hygiene Law status if applicable: 9.41 by PD, 9.45 by Director of Community Services, or voluntary. Involuntary transport: capacity determination and PD role documented plainly.}
Restraints [none / soft ___ points at ___ by ___, supine, PMS q___, reason: ___]. Sedation [none / see Tox agitated fork, documented there].
Pt transported [voluntarily / involuntarily under ___] to ___ {Comprehensive Psychiatric Emergency Program-capable ED if that drove the destination}.
**Escalation line:** Pt remained [calm and cooperative / ___] throughout. Medical causes screened: BGL ___, no acute medical findings / [medical cause suspected: ___, see ___ block].

---

## 13. BURNS / ELECTRICAL BLOCK
Categories: Burns, Electrocution
Escalates to: Trauma Major on any RED criterion (burns + trauma go to trauma center). CO/hazmat fork of Tox for inhalation. Cardiac 2b for post-electrical dysrhythmia. Cardiac Arrest template if pulses lost.

Source: ___ {flame, scald, chemical ___, electrical ___ V AC/DC, contact time ___, lightning}. Enclosed space [Y, duration ___ / N]. Burning stopped by ___ at ___. Scene [safe / utility secured by ___].
Burns: ___ {degree, location, circumferential Y/N}, ___% BSA (rule of nines: ___) {first-degree excluded from BSA}. Airway: [no facial burns, singed nasal hair, soot, or voice change / ___: airway burn suspected]. {CO considered: SpCO ___ / see Tox CO fork.}
{Electrical:} Entry ___, exit ___, [LOC / tetany / fall from ___]. Monitor at ___: ___ {rhythm; dysrhythmia → add Cardiac 2b}. 12-lead at ___: ___. {Lightning/high voltage: c-spine per Trauma criteria.}
Rings/constricting items removed at ___. Dressings: [dry sterile / moist sterile (≤10% BSA, for pain) ]. {Chemical: flushed ___ min with ___; dry powder brushed first.} {Eye: irrigated with NS, copious, started at ___; tetracaine 2 gtt at ___ q5 prn.}
IV ___g ___ x [1 / 2] at ___. NS 500 mL bolus at ___, reassessed ___. Hypothermia prevention ___ {>10% BSA: dry dressings only, pt kept warm}.
Analgesia: fentanyl ___ mcg at ___, pain ___ to ___ / ketamine ___ at ___ / withheld: ___.
Destination: [ED ___ / trauma center (burns + trauma) / burn center per med control, cited above].
**Escalation line:** [Airway patent and voice unchanged throughout, rhythm ___ / airway involvement progressed at ___ / dysrhythmia ___, see Cardiac 2b. RED criteria: none / MET ___, Trauma Major.]

---

## 14. DOA BLOCK
Categories: DOA (attended), DOA (Unattended)
No escalation. If criteria are NOT met, this block does not apply: work the arrest on the Cardiac Arrest template.

Found: ___ yo [M/F] [in bed / ___], last known alive ___ per ___. Pt pulseless and apneic, assessed at ___.
Obvious death criteria: ___ {ANY one, name what you saw: body decomposition / rigor mortis / dependent lividity / injury incompatible with life: ___ / pulseless + apneic with no organized activity on ECG after significant blunt or penetrating trauma meeting RED criteria / submersion >1 hr} OR valid [MOLST / eMOLST / DNR] presented at ___, verified by ___ {form location, signatures}.
{ALS strip if used:} Monitor applied at ___: [asystole confirmed in ___ leads / no organized activity], strip attached. {Not required for obvious-death criteria; say why no strip if none.}
Resuscitation [not initiated / initiated by ___ and discontinued at ___ per criteria above; pads and equipment left in place].
{Hypothermia caveat: criteria differ in severe hypothermia; if cold, say why criteria still applied or why you worked it.}
PD notified at ___, [on scene ___ / ETA ___]. Scene [undisturbed / pt covered / moved to ___ with PD permission]. {Attended:} Pt under care of [hospice ___ / MD ___], contacted at ___, ___. Family on scene: ___, informed by ___.
Time of determination: ___. 35M___ [remained on scene until ___ / released by PD at ___]. 35M___ returned to service.
{This block replaces the treatment sections AND the disposition. Nothing else follows it.}

---

## 15. ENVIRONMENTAL BLOCK
Categories: Drowning, Heat/Cold Exposure
Escalates to: Cardiac Arrest template (hypothermic arrest: say resuscitation continued, cold caveats applied). Respiratory block for post-drowning respiratory distress. Trauma if mechanism involved.

Exposure: ___ {environment, temp if known, duration, wet/dry, clothing}. Found by ___.

{Heat, normal mental status:} Skin [elevated temp / normal], pt moved to cool environment at ___, clothing loosened, [oral hydration / cold packs to palms, soles, neck, groin, axillae at ___, skin kept wet].
{Heat, AMS:} Elevated skin temp with GCS ___: active whole-body cooling initiated at ___ via ___ {in order of preference: ice/cold water immersion, TACO, cold dousing, cold-soaked towels + ice packs}, continued until mental status returned at ___ / continued through txp. {Transport delayed for cooling: say so and why, it's protocol.} NS 500 mL bolus at ___, repeated ___ {to 2 L, no pulmonary edema}.
{Cold:} Core/axillary temp ___ if obtained. [Mild: shivering, alert / moderate: ___ / severe: ___]. Wet clothing removed at ___, passive rewarming ___, handled gently {rough handling → VF}. [Localized: part ___, [rewarmed with ___ / not field-rewarmed: refreezing risk], not rubbed].
{Drowning:} Submersion ___ min in ___ {water type/temp}, [witnessed / unwitnessed], extricated by ___ at ___. [Breathing on our arrival / resuscitated by ___]. L/S ___, SpO2 ___, ETCO2 ___. [C-spine per criteria: ___]. {Every symptomatic submersion gets transport advised: delayed pulmonary edema named in the RMA risk line if pt refuses.}
Pt reassessed at ___: GCS ___, temp trend ___, L/S ___.
**Escalation line:** [Stable/improving throughout / deteriorated at ___: ___. Switch to ___ template.]

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

G___ P___, ___ wks by [dates / ultrasound / pt report], prenatal care [Y, ___ / N]. Complications this pregnancy ___ {HTN, gestational diabetes mellitus, previa, multiples}. {>20 wks: pt positioned left lateral recumbent / uterus manually displaced leftward at ___.}
Presenting: ___ {contractions q___ min x ___ sec since ___, rupture of membranes at ___ [clear / meconium], bleeding ___, urge to push [Y/N], fetal movement ___}.
{Pre-eclampsia screen, >20 wks to 6 wks postpartum:} BP ___ [≥160/110 / 140-159 or 90-109 with: severe headache / visual changes / RUQ or epigastric pain / none]. [Screen negative / PRE-ECLAMPSIA: mag 4 g in 100 mL IV over 20 min started at ___] [ECLAMPSIA, seizing: mag as above + Neuro seizure fork, midazolam documented there].
{Delivery imminent:} Crowning at ___. Delivery at ___: [vertex / ___], nuchal cord [none / reduced x___], infant [suctioned as needed / stimulated], APGAR ___ at 1 min, ___ at 5 min. Cord clamped and cut at ___ {≥1 min after delivery}, infant placed skin-to-skin on mother's chest, then dried/wrapped for txp. Placenta [delivered at ___, transported / undelivered].
{Postpartum hemorrhage:} estimated blood loss ___, [firm fundus after massage at ___ / boggy]. Fundal massage at ___. {Per OB Hemorrhagic Shock protocol:} NS bolus ___ at ___. Oxytocin not carried; med control contacted at ___ for ___ / TXA ___ per med control. SBP ___ to ___.
Two patients documented from delivery forward: [infant assessment in linked PCR ___ / infant care transferred to ___].
**Escalation line:** [Uncomplicated, mother and infant stable / pre-eclampsia treated as above, BP ___ on reassessment / postpartum hemorrhage: interventions above, hospital notified of unstable OB at ___]. Destination [ED / L&D-capable ___ per ___].

---

## 18. POLICE ASSIST BLOCK
Categories: Blood Draw Request, Law Enforcement Blood Draw, Medication Administration (Assist PD), EMS Requested by Law Enforcement
The chart here is as much legal record as medical record. Times, names, badge numbers, and what was NOT done carry the weight.

Requested by [___ PD, Officer ___, badge ___] at ___ for ___.
{LE blood draw:} Draw performed under [pt consent, witnessed by ___ / court order presented, reviewed at ___ / ___ per agency policy]. Pt [cooperative / ___]. Site ___ cleaned with [non-alcohol prep ___]. Kit: [PD-supplied kit, sealed, lot ___], tubes x___, drawn at ___, handed directly to Officer ___ at ___, chain of custody form [signed / ___]. No medical complaint voiced; [assessment offered and declined, see RMA / assessed: ___].
{Medication administration assist:} Medication ___ administered at ___ under ___ {standing order / med control Dr. ___}, indication ___, response ___. Custody status ___. Documented assessment before and after: ___.
{EMS requested by LE, subject in custody:} Subject assessed at ___: ___ {injuries or complaints, or "denies injury or complaint"}. [Tase/OC/restraint exposure: probes removed by ___, sites ___, ___]. [Fit for incarceration NOT determined by EMS; pt advised and PD advised transport available / pt transported / RMA with PD witness ___].
**Escalation line:** [No medical complaint identified, no treatment indicated / clinical issue found: ___, see ___ block].

---

## 19. TRAUMA MINOR / MUSCULOSKELETAL BLOCK
Categories: Animal Bite, Back Pain, Eye Problem, Foot Injury, Fracture/Dislocation, Hemorrhage/Laceration, Pain (extremities), Soft Tissue Injury
Escalates to: Trauma General/Major if MOI or findings say so (field triage criteria reviewed and negative is the load-bearing line here).
{Spinal motion restriction/c-spine: covered by the shell Primary line for this block.}

MOI: ___ {low-energy, in one clause}. Time of injury ___.
Injury: ___ {what, where, side, size for wounds}. Distal PMS [intact / ___] before and after any splint. [Deformity / swelling / ecchymosis / wound edges ___ / none] {any that apply}.
{Bite:} Animal ___, [provoked / unprovoked], owner ___ {known, vaccination status ___ / unknown/stray}, [animal control / PD] notified at ___. Wound irrigated with ___ at ___.
{Eye:} Visual acuity [grossly intact / ___ ], [no globe injury evident / ___]. Irrigation ___ / tetracaine 2 gtt at ___ / not indicated. {Penetrating globe: no pressure, shield, escalate.}
{Back pain, atraumatic red flags screened:} [no saddle anesthesia, no new incontinence/retention, no bilateral leg weakness, no fever, no anticoagulants, no cancer Hx / ___: escalate DDx].
Wound care: [irrigated / dressed ___ / bleeding controlled with direct pressure at ___]. Splint: ___ {type, position} at ___, PMS rechecked ___ / not indicated.
Analgesia: [acetaminophen 1000 mg PO / ibuprofen 400 mg PO {not if >60, anticoagulated, renal, pregnant} / ketorolac 15 mg at ___ {same limits} / fentanyl ___ mcg at ___ / none, pain ___/10, pt declined].
Field triage criteria reviewed: [no RED or YELLOW criteria].
**Escalation line:** [Isolated ___ injury, no triage criteria met / criteria MET: ___, see Trauma General/Major].

---

# DEDICATED TEMPLATES
Full narratives. The shell's dispatch/arrival opening and disposition close still wrap them; the template replaces everything in between. Doses per v26.1.

## 20. TEMPLATE: CARDIAC ARREST (medical)
{Also the base for Traumatic Arrest: complete this template and add section 20a.}

Arrest [witnessed by ___ at ___ / unwitnessed, last known alive ___ per ___]. Estimated downtime ___. Bystander CPR [by ___ from ___ / none]. AED [applied by ___, ___ shocks delivered / none] prior to arrival.
Upon 35M# arrival ___: pt pulseless, apneic. Obvious death criteria reviewed: not met {if met, this is the DOA block, stop}. [DNR/MOLST: none presented / presented and did not preclude resuscitation: ___].
Compressions [continued / initiated] at ___. Initial rhythm on monitor at ___: [VF / pulseless VT / asystole, confirmed in ___ leads / PEA, rate ___].
CPR per AHA: 100-120/min, rotated q2 min, interruptions minimized, mechanical CPR device [applied by ___, rate set to 30:2 / Continuous].
Defibrillation: ___ J at ___, ___, ___ {each shock, time}. [Vector change to anterior/posterior at ___ for refractory VF/VT / n/a].
Airway: [OPA/NPA + BVM with O2 / iGel ___ at ___ / ETT ___ at ___, ___ attempts, depth ___ cm], placement confirmed by waveform capnography, ETCO2 ___. After advanced airway: continuous compressions, 8-10 breaths/min.
Access: [IV ___g ___ / IO ___] at ___. BGL ___.
Epi 1 mg (0.1 mg/mL) IV/IO at ___, ___, ___, ___, ___ {q3-5 min, max 5; list times}.
{Shockable:} [Amiodarone 300 mg IV at ___, repeat 150 mg at ___ / Lidocaine ___ mg IV at ___ {1.5 mg/kg}, repeat ___ mg at ___ {0.75 mg/kg}]. {Torsades/hypomag:} Mag 2 g IV at ___.
{PEA/asystole:} NS 500 mL bolus at ___. {Suspected hyperkalemia (dialysis, Hx):} Sodium bicarb 50 mEq IV at ___, calcium chloride 1 g IV at ___, ≥50 mL NS flushed between.
Reversible causes addressed: ___ {H's & T's actually searched: BGL ___, volume ___, hypoxia ___, tension pneumo [decompressed ___ / not suspected], tox ___, hyperK ___}.
Rhythm checks q2 min: ___ {sequence with times, or "per code summary, attached"}. {Monitor data/code summary attached, as with every assessed or treated pt.}

[ROSC at ___: pulses at ___, rhythm ___, BP ___. 12-lead at ___: ___ {STEMI → PCI-capable destination}, transmitted. NS to maintain SBP >100 / MAP >65: ___ mL, L/S ___. Norepi 2-20 mcg/min started at ___ / push-dose epi 10-20 mcg q3-5 at ___, ___ / not needed. Sedation for airway per protocol: ___. Re-arrest [none / at ___, resumed above]. Hospital notified of ROSC at ___.]

[No ROSC: TOR criteria at ___: age ≥18 [Y], arrest unwitnessed by bystanders and EMS [Y/N], no bystander CPR [Y/N], no shocks delivered [Y/N], no ROSC at any point [Y/N], ≥20 min resuscitation [Y, ___ min], hypothermia not suspected [Y]. Med control contacted at ___ (≈20 min mark per practice), Dr. ___, criteria reported, orders: [terminate at ___ / continue: ___]. {All seven standing-order criteria met and termination on standing order instead: say so.} ETCO2 at termination discussion: ___. Tubes and lines left in place. PD notified at ___. Family present: ___, supported by ___. Pt moved to ___ with PD permission / left in place.]

## 20a. TRAUMATIC ARREST ADDENDUM
MOI: ___ {blunt/penetrating, RED criteria met: ___}. {Blunt or penetrating trauma + no organized activity on ECG = obvious death criterion: if that was the case, DOA block, not this template.}
Organized activity on initial ECG: [Y, rate ___ / N but mechanism inconsistent with traumatic cause, worked as medical].
Trauma-specific interventions, in order done: bilateral chest decompression [___ ICS ___ line R at ___, L at ___, result ___ / not indicated], hemorrhage control ___ {TQ/packing, times}, pelvic binder ___, airway with c-spine ___.
Volume: NS ___ via [IV x2 / IO] at ___.
Destination if ROSC: trauma center ___. TOR: traumatic arrests follow the same criteria; med control contact ___ documented above.

## 21. TEMPLATE: STEMI
{Starts as Cardiac 2a; from the moment criteria fire, this replaces it.}

12-lead at ___: ST elevation ___ mm in ___ {leads}, [reciprocal depression ___ / none], [new LBBB]. STEMI identified at ___. {Inferior: R-sided 12-lead at ___: [RV involvement ___ / negative].}
STEMI alert called to ___ at ___, 12-lead transmitted at ___, [confirmed by Dr. ___ / transmitted, unconfirmed].
Destination: ___ {PCI-capable, ETA ___ min from pt contact; <90 min window [met / not met, med control consulted: ___]}.
Defib pads placed at ___. ASA 324 mg chewed at ___ / given prior / withheld: ___.
NTG 0.4 mg SL x___ at ___, SBP ___ before each {>120 or MAP >90 required; withheld: ___ {SBP, RV involvement, phosphodiesterase-5 inhibitor}}.
IV ___g ___ at ___. {SBP <100: supine, NS 500 mL at ___, repeated ___ {to 2 L, L/S clear, goal SBP >100}.}
Fentanyl ___ mcg at ___ for pain ___ unrelieved by NTG, ___ to ___ / withheld: ___.
{Med control adds:} Metoprolol 5 mg slow IV at ___ per Dr. ___ {HR >80 and SBP >120} / none.
Serial 12-lead at ___: ___. Reassessed en route q___: pain ___, rhythm ___ {watch for blocks and VF, pads already on}.
Prenote update to ___ at ___: ETA ___, [cath lab activated per receiving RN / ___]. {If arrest en route: Cardiac Arrest template from that timestamp.}

## 22. TEMPLATE: RESPIRATORY ARREST / FAILURE
{Apneic or RR <10 / ineffective respirations with a pulse. If pulses lost: Cardiac Arrest template from that timestamp.}

Found: [apneic / RR ___, ineffective: ___ {cyanosis, retractions, AMS}], pulse [present, rate ___]. SpO2 ___, ETCO2 ___.
Airway opened [head-tilt chin-lift / jaw thrust] at ___, suctioned ___, [visible obstruction removed: ___ / FBAO suspected → laryngoscopy at ___, Magill at ___, result ___ / clear].
BVM with O2 initiated at ___, q5-6 sec, visible chest rise [Y / difficult: ___]. [OPA / NPA] placed at ___.
Suspected cause: ___ {opioid → naloxone ___ at ___ per Tox block dosing, response ___ / CHF / COPD / asthma → see block treatments given: ___ / neuro / other}.
[Ventilation effective with BLS airway, advanced airway deferred / Advanced airway at ___: [iGel ___ / ETT ___, ___ attempts, ___ cm], confirmed by waveform capnography ETCO2 ___ and ___ {auscultation, chest rise}, secured, re-verified after every move: ___.]
Post-airway management: ventilation rate ___, SpO2 ___ to ___, ETCO2 ___ to ___. Sedation/analgesia for airway tolerance: [midazolam ___ at ___ / fentanyl ___ at ___ / not required: ___] {per post-intubation protocol}.
Reassessed q___: [spontaneous respirations returned at ___, RR ___, supported with ___ / ventilated throughout]. Pulse [maintained / LOST at ___ → Cardiac Arrest template].
Hospital notified at ___ of [ventilated pt / airway in place], RN ___.

## 23. TEMPLATE: STROKE / CVA
{Neuro block fires positive → this.}

LKW ___ per ___ {name/relationship, contact collected: ___}. Symptom onset ___ if witnessed, by ___. Onset-to-ED estimate ___ {<3.5 hr → NYS-designated stroke center required}.
Deficits found at ___: ___ {each named: facial droop ___ side, arm drift ___, speech ___, gaze, neglect, visual field}.
NYS-LAMS Score: ___/6 {droop ___, drift ___, speech ___, grip ___}.
BGL ___ {<60 treated per Metabolic block: ___, deficits [resolved → not a stroke alert, chart it / persist]}. Anticoagulated [Y ___ / N]. Recent surgery/trauma/GI bleed [___ / none reported]. Seizure at onset [Y / N].
Stroke alert called to ___ at ___ with LKW and NYS-LAMS. Destination: [NYS-LAMS 0-3: ___ {NYS stroke center} / NYS-LAMS 4-6: exclusions reviewed, ___ {thrombectomy-capable}], txp decision per ___ {protocol / med control Dr. ___}.
IV ___g ___ at ___ {no delays for access}. SBP ___ [maintained >120 / >220 or DBP >120: med control at ___, orders ___]. Head of stretcher ___. NPO.
Serial neuro at ___ and ___: [unchanged / evolving: ___]. {Deficits resolving en route: documented as ___, alert NOT cancelled by EMS.}
Prenote update at ___: ETA, deficits, LKW, family [following / contact ___ given to RN ___].

## 24. TEMPLATE: ACTIVE SHOOTER / VIOLENT INCIDENT
{Operational narrative. Clinical care per patient goes on that patient's PCR with the right block; this template is for the incident-role chart. RTF is regionalized and no county-level plan exists: default posture is staged until PD declares the scene, and this chart documents exactly that.}

35M___ [dispatched / self-dispatched per ___] to reported active shooter at ___ at ___. Staged at ___ {location} at ___ per [dispatch / IC]. Scene declared [unsecured / warm zone established at ___ / secured at ___] by ___ {PD/IC}.
ICS: incident command ___ at ___, 35M___ assigned [staging / casualty collection point at ___ / treatment / transport] by ___ at ___. Unified command [Y/N]. MCI [declared at ___, level ___ → MCI template supplements / not declared].
Entry: [remained staged, no pt contact, released at ___ by ___ / entered warm zone at ___ with ___ {LE escort/RTF}, PPE ___].
Care rendered under [TECC/warm zone constraints]: ___ {hemorrhage control, airway positioning, rapid extraction; interventions deliberately deferred to CCP/cold zone: ___}. Pts moved to CCP at ___.
Patients treated/transported by 35M___: ___ {triage tag #s; each gets own PCR, cross-referenced}.
Accountability: crew ___ / ___, both accounted for at ___. Released from incident by ___ at ___.

## 25. TEMPLATE: MCI
{Incident-role chart. Each transported pt still gets a PCR; abbreviated per MCI standard, cross-referenced by triage tag #.}

MCI declared at ___ by ___ for ___ {incident}, estimated ___ pts. Level ___ per ___.
35M___ arrived ___, assigned [triage / treatment / transport / staging / medical branch] by IC ___ at ___.
Triage system: START. Pts triaged by 35M___: ___ {counts by category: Red ___, Yellow ___, Green ___, Black ___}.
{Triage role:} Triage completed at ___, counts reported to ___. No treatment during triage beyond [airway positioning / hemorrhage control] per START: ___.
{Treatment role:} Treatment area at ___, pts received ___, interventions ___ {by tag #}.
{Transport role:} Destinations coordinated with ___ {hospital/MedCom}: ___ {tag # → hospital, ordered by priority}. Hospital capacity confirmed via ___.
Pt(s) transported by 35M___: tag # ___, [category], ___ {one line of clinical course each; full detail in that pt's PCR}.
Documentation standard: abbreviated PCRs per regional MCI procedure, completed [during / after] incident; this narrative cross-references tag #s ___.
Released by ___ at ___. Demobilized, unit restocked at ___, returned to service ___.

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
