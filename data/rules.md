version: "3.1"

rules:

- rule: Say goodbye anytime the user says goodbye
  steps:
  - intent: goodbye
  - action: utter_goodbye

- rule: Say अलविदा anytime the user says अलविदा
  steps:
  - intent: goodbye_hindi
  - action: utter_goodbye_hindi

- rule: Say निरोप anytime the user says निरोप
  steps:
  - intent: goodbye_marathi
  - action: utter_goodbye_marathi

- rule: Say వీడ్కోలు anytime the user says వీడ్కోలు
  steps:
  - intent: goodbye_telugu
  - action: utter_goodbye_telugu

- rule: Say 'I am a bot' anytime the user challenges
  steps:
  - intent: iamabot
  - action: utter_iamabot

- rule: Say 'मैं एक बोट हूँ' anytime the user challenges
  steps:
  - intent: iamabot_hindi
  - action: utter_iamabot_hindi

- rule: Say 'मी एक बोट आहे' anytime the user challenges
  steps:
  - intent: iamabot_marathi
  - action: utter_iamabot_marathi

- rule: Say 'నేనొక రోబోని' anytime the user challenges
  steps:
  - intent: iamabot_telugu
  - action: utter_iamabot_telugu

- rule: answer out of scope
  steps:
  - intent: out_of_scope
  - action: utter_out_of_scope

- rule: answer out of scope hindi
  steps:
  - intent: out_of_scope_hindi
  - action: utter_out_of_scope_hindi

- rule: answer out of scope marathi
  steps:
  - intent: out_of_scope_marathi
  - action: utter_out_of_scope_marathi

- rule: answer out of scope telugu
  steps:
  - intent: out_of_scope_telugu
  - action: utter_out_of_scope_telugu
