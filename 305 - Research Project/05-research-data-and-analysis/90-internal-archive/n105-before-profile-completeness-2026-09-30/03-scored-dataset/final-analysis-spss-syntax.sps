* Hybrid Learning and Training Effectiveness at Union Bank of India.
* Stage 3 syntax: 105 eligible response records.
* Set SPSS's working directory to the folder that contains final-analysis-data.csv before running.

GET DATA
  /TYPE=TXT
  /FILE='final-analysis-data.csv'
  /ENCODING='UTF8'
  /DELCASE=LINE
  /DELIMITERS=','
  /QUALIFIER='"'
  /ARRANGEMENT=DELIMITED
  /FIRSTCASE=2
  /IMPORTCASE=ALL
  /VARIABLES=
    response_id A15
    source A10
    age_group A15
    service_length A20
    job_level A12
    imputation_count F8.0
    flag_count F8.0
    HL1 F8.3
    HL2 F8.3
    HL3 F8.3
    HL4 F8.3
    HL5 F8.3
    HL6 F8.3
    HL7 F8.3
    TC1 F8.3
    TC2 F8.3
    TC3 F8.3
    TC4 F8.3
    TC5 F8.3
    TC6 F8.3
    LE1 F8.3
    LE2 F8.3
    LE3 F8.3
    LE4 F8.3
    LE5 F8.3
    LE6 F8.3
    TE1 F8.3
    TE2 F8.3
    TE3 F8.3
    TE4 F8.3
    TE5 F8.3
    TE6 F8.3
    TE7 F8.3
    Hybrid_Learning F8.6
    Trainer_Competence F8.6
    Learner_Engagement F8.6
    Training_Effectiveness F8.6.
EXECUTE.

VALUE LABELS source 'manual' 'Printed questionnaire' 'digital' 'Google Forms'.
VARIABLE LABELS
  Hybrid_Learning 'Arithmetic mean of HL1 to HL7'
  Trainer_Competence 'Arithmetic mean of TC1 to TC6'
  Learner_Engagement 'Arithmetic mean of LE1 to LE6'
  Training_Effectiveness 'Arithmetic mean of TE1 to TE7'.
FORMATS HL1 TO TE7 (F8.3) Hybrid_Learning TO Training_Effectiveness (F8.6).

* Profile and item description.
FREQUENCIES VARIABLES=age_group service_length job_level.
DESCRIPTIVES VARIABLES=HL1 TO TE7 Hybrid_Learning Trainer_Competence Learner_Engagement Training_Effectiveness
  /STATISTICS=MEAN STDDEV MIN MAX.

* Reliability for the four item sets.
RELIABILITY /VARIABLES=HL1 TO HL7 /SCALE('Hybrid Learning') ALL /MODEL=ALPHA.
RELIABILITY /VARIABLES=TC1 TO TC6 /SCALE('Trainer Competence') ALL /MODEL=ALPHA.
RELIABILITY /VARIABLES=LE1 TO LE6 /SCALE('Learner Engagement') ALL /MODEL=ALPHA.
RELIABILITY /VARIABLES=TE1 TO TE7 /SCALE('Training Effectiveness') ALL /MODEL=ALPHA.

* Primary tests of H1 to H3: two-tailed Pearson correlations at the 5 per cent level.
CORRELATIONS /VARIABLES=Hybrid_Learning Trainer_Competence Learner_Engagement Training_Effectiveness
  /PRINT=TWOTAIL SIG /MISSING=PAIRWISE.

* Supporting regression model: Hybrid Learning and Trainer Competence in relation to Learner Engagement.
REGRESSION /DEPENDENT Learner_Engagement
  /METHOD=ENTER Hybrid_Learning Trainer_Competence
  /STATISTICS=COEFF R ANOVA COLLIN TOL.

* Supporting regression model: Learner Engagement in relation to Training Effectiveness.
REGRESSION /DEPENDENT Training_Effectiveness
  /METHOD=ENTER Learner_Engagement
  /STATISTICS=COEFF R ANOVA.

* Do not interpret these outputs as causal or as a formal mediation test.
