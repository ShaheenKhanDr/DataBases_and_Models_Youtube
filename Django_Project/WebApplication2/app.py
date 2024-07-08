from flask import Flask, render_template, request

app = Flask(__name__)

def find_remedy(selected_symptoms):
    remedies = {
        "ignatia amara": {"acute", "depression", "constant", "sadness", "weeping spells", "isolation",
                          "deep thoughts", "irritability", "dull mind", "weak memory", "excessive weakness",
                          "acute grief", "broken relationships", "life disappointments", "bipolar disorder"},
        "natrum mur": {"sensitive individuals", "sporadic episodes", "weeping",
                       "absorbed in grief", "dwelling on painful memories",
                       "do not like consolation", "worsens complaints", "easy offender",
                       "lacks interest in work", "managing depression",
                       "women before menstruation"},
        "aurum met": {"extreme sadness", "hopelessness", "constant suicidal thoughts", "feeling worthless",
                      "negative thoughts", "dark future perception", "life as a burden"},
        "kali phos": {"over-stressed", "anxious", "constant sadness", "negative thoughts", "reduce mental",
                      "physical exhaustion", "anxiety attacks", "weeping spells", "sleeplessness"},
        "natrum sulph": {"overwhelming suicidal thoughts", "sadness", "weeping", "irritability", "morning sadness",
                         "aversion to talking", "indifference towards family", "frequent thoughts to end life",
                         "confusion", "difficulty in thinking"},
        "sepia": {"menopause depression", "sadness", "aversion to family", "loss of interest in work",
                  "indifferent behavior towards life and family", "constant worry and stress", "irritation",
                  "easy offending", "sporadic weeping spells", "seeking consolation and sympathy",
                  "loss of sexual desire", "depression triggered after childbirth"},
        "cimicifuga racemosa": {"post-childbirth depression", "extreme sadness", "darkness symptoms", "exhaustion",
                                "excessive talking", "indifferent behavior", "fear of death", "fear of mental insanity"},
        "lachesis": {"depression with delusion", "psychotic depression", "sadness", "feelings of abandonment",
                     "excessive talkativeness", "delusions", "frequent switching of subjects", "violent anger",
                     "madness", "delusions causing suspicion", "fear of harm", "restlessness", "aversion to work",
                     "evasion from the world"},
        "coffea crude": {"manages sleeplessness", "constant thoughts leading to sleeplessness", "nighttime restlessness",
                         "tossing and turning", "mood changes", "irritability", "anxiety", "weeping", "weakness"},
        "arsenic album": {"anxiety and sadness", "accompany sadness", "anxiety about health and future",
                          "intense restlessness", "marked weakness", "fears of disease", "financial loss",
                          "loneliness", "death"}
    }

    selected_symptoms_set = set(selected_symptoms)
    best_match = None
    max_matches = 0

    for remedy, symptoms in remedies.items():
        matches = len(selected_symptoms_set.intersection(symptoms))
        if matches > max_matches:
            max_matches = matches
            best_match = remedy

    return best_match if best_match else "Remedy not found for the given signs and symptoms."

@app.route('/')
def index():
    symptoms = ["acute", "depression", "constant", "sadness", "weeping spells", "isolation",
                "deep thoughts", "irritability", "dull mind", "weak memory", "excessive weakness",
                "acute grief", "broken relationships", "life disappointments", "bipolar disorder",
                "sensitive individuals", "sporadic episodes", "weeping", "absorbed in grief",
                "dwelling on painful memories", "do not like consolation", "worsens complaints",
                "easy offender", "lacks interest in work", "managing depression", "women before menstruation",
                "extreme sadness", "hopelessness", "constant suicidal thoughts", "feeling worthless",
                "negative thoughts", "dark future perception", "life as a burden", "over-stressed",
                "anxious", "reduce mental exhaustion", "physical exhaustion", "anxiety attacks",
                "morning sadness", "aversion to talking", "indifference towards family", "frequent thoughts to end life",
                "confusion", "difficulty in thinking", "menopause depression", "loss of interest in work",
                "indifferent behavior towards life and family", "constant worry and stress", "irritation",
                "easy offending", "sporadic weeping spells", "seeking consolation and sympathy",
                "loss of sexual desire", "depression triggered after childbirth", "post-childbirth depression",
                "extreme sadness", "darkness symptoms", "exhaustion", "excessive talking", "indifferent behavior",
                "fear of death", "fear of mental insanity", "depression with delusion", "psychotic depression",
                "feelings of abandonment", "excessive talkativeness", "frequent switching of subjects", "violent anger",
                "madness", "delusions causing suspicion", "fear of harm", "restlessness", "aversion to work",
                "evasion from the world", "manages sleeplessness", "constant thoughts leading to sleeplessness",
                "nighttime restlessness", "tossing and turning", "mood changes", "anxiety", "weeping", "weakness",
                "anxiety and sadness", "anxiety about health and future", "intense restlessness", "marked weakness",
                "fears of disease", "financial loss", "loneliness", "death"]
    return render_template('index.html', symptoms=symptoms)

@app.route('/get_remedy', methods=['POST'])
def get_remedy():
    selected_symptoms = request.form.getlist('symptoms')
    remedy = find_remedy(selected_symptoms)
    symptoms = ["acute", "depression", "constant", "sadness", "weeping spells", "isolation",
                "deep thoughts", "irritability", "dull mind", "weak memory", "excessive weakness",
                "acute grief", "broken relationships", "life disappointments", "bipolar disorder",
                "sensitive individuals", "sporadic episodes", "weeping", "absorbed in grief",
                "dwelling on painful memories", "do not like consolation", "worsens complaints",
                "easy offender", "lacks interest in work", "managing depression", "women before menstruation",
                "extreme sadness", "hopelessness", "constant suicidal thoughts", "feeling worthless",
                "negative thoughts", "dark future perception", "life as a burden", "over-stressed",
                "anxious", "reduce mental exhaustion", "physical exhaustion", "anxiety attacks",
                "morning sadness", "aversion to talking", "indifference towards family", "frequent thoughts to end life",
                "confusion", "difficulty in thinking", "menopause depression", "loss of interest in work",
                "indifferent behavior towards life and family", "constant worry and stress", "irritation",
                "easy offending", "sporadic weeping spells", "seeking consolation and sympathy",
                "loss of sexual desire", "depression triggered after childbirth", "post-childbirth depression",
                "extreme sadness", "darkness symptoms", "exhaustion", "excessive talking", "indifferent behavior",
                "fear of death", "fear of mental insanity", "depression with delusion", "psychotic depression",
                "feelings of abandonment", "excessive talkativeness", "frequent switching of subjects", "violent anger",
                "madness", "delusions causing suspicion", "fear of harm", "restlessness", "aversion to work",
                "evasion from the world", "manages sleeplessness", "constant thoughts leading to sleeplessness",
                "nighttime restlessness", "tossing and turning", "mood changes", "anxiety", "weeping", "weakness",
                "anxiety and sadness", "anxiety about health and future", "intense restlessness", "marked weakness",
                "fears of disease", "financial loss", "loneliness", "death"]
    return render_template('index.html', symptoms=symptoms, remedy=remedy)

if __name__ == '__main__':
    app.run(debug=True)
