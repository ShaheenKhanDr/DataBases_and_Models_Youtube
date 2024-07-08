# Let's handle duplication to ensure each sign or symptom is only considered once.
# Let's define a function firsthand
def find_remedy():

    # Let’s set a prompt to the User inputs
    signs_symptoms = input("Enter the signs and symptoms of the patient: ")

    # Let's convert signs and symptoms into a set of unique words.
    unique_signs_symptoms = set(signs_symptoms.lower().split())

    # Let's compile a dictionary holding every indication as a unique word
    remedies = {
        "ignatia amara": {"acute", "depression", "constant", "sadness", "weeping", "spells", "isolation", "deep", "thought", "irritability", "dull", "mind", "weak", "memory", "excessive", "weakness", "acute", "grief", "broken", "relationships", "life", "disappointments", "bipolar", "disorder"},
        "natrum mur": {"sensitive", "individuals", "with", "sporadic", "episodes", "of", "weeping", "suitable", "for", "those", "absorbed", "in", "grief", "dwelling", "on", "painful", "past", "memories", "do", "not", "like", "consolation", "worsens", "complaints", "easy", "offender", "lacks", "interest", "in", "work", "beneficial", "for", "managing", "depression", "in", "women", "before", "menstruation"},
        "aurum met": {"extreme", "sadness", "and", "hopelessness", "constant", "suicidal", "thoughts", "feeling", "worthless", "and", "of", "no", "value", "Negative", "thoughts", "dark", "future", "perception", "life", "as", "a", "burden", "constant", "suicidal", "thoughts"},
        "kali phos": {"over-stressed", "anxious", "constant", "sadness", "negative", "thoughts", "reduce", "mental", "and", "physical", "exhaustion", "anxiety", "attacks", "weeping", "spells", "and", "sleeplessness"},
        "natrum sulph": {"overwhelming", "suicidal", "thoughts", "sadness", "weeping", "and", "irritability", "morning", "sadness", "is", "most", "severe", "aversion", "to", "talking", "indifference", "towards", "family", "frequent", "thoughts", "to", "end", "life", "confusion", "and", "difficulty", "in", "thinking"},
        "sepia": {"menopause", "depression", "sadness", "aversion", "to", "family", "loss", "of", "interest", "in", "work", "indifferent", "behavior", "towards", "life", "and", "family", "constant", "worry", "and", "stress", "irritation", "and", "easy", "offending", "sporadic", "weeping", "spells", "seeking", "consolation", "and", "sympathy", "loss", "of", "sexual", "desire", "depression", "triggered", "after", "childbirth"},
        "cimicifuga racemosa": {"post-childhood", "depression", "known", "for", "treating", "extreme", "sadness", "and", "darkness", "symptoms", "include", "exhaustion", "excessive", "talking", "indifferent", "behavior", "fear", "of", "death", "and", "fear", "of", "mental", "insanity"},
        "lachesis": {"depression", "with", "delusion", "like", "psychotic", "depression", "sadness", "feelings", "of", "abandonment", "excessive", "talkativeness", "delusions", "frequent", "switching", "of", "subjects", "violent", "anger", "and", "madness", "delusions", "can", "cause", "suspicion", "and", "fear", "of", "harm", "restlessness", "aversion", "to", "work", "and", "evasion", "from", "the", "world"},
        "coffea crude": {"manages", "sleeplessness", "identifies", "constant", "thoughts", "leading", "to", "sleeplessness", "manifests", "as", "nighttime", "restlessness", "with", "tossing", "and", "turning", "mood", "changes", "irritability", "anxiety", "weeping", "and", "weakness"},
        "arsenic album": {"anxiety", "and", "sadness", "accompany", "sadness", "anxiety", "about", "health", "and", "future", "intense", "restlessness", "marked", "weakness", "fears", "of", "disease", "financial", "loss", "loneliness", "and", "death"}
    }

# Let's initialize an empty list named `matched_remedies` to store remedies that match the user's entered signs and symptoms.
    matched_remedies = []

# Let's set the loop for mapping over remedies and its indications.
    for remedy, symptoms in remedies.items():
        if symptoms.intersection(unique_signs_symptoms):
            matched_remedies.append(remedy)

    if matched_remedies:
        return matched_remedies
    else:
        return "Remedy not found for the given signs and symptoms."


# Test the modified function.
remedies = find_remedy()
print("Remedies:", remedies)
