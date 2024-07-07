# Python Medical Project “MDSS_GUI”
# Let's Start a Graphical User Interface.
import tkinter as tk
from tkinter import messagebox


# Let's define a function that takes a single argument 'signs_symptoms' to represents the indications of a patient.
def find_remedy(signs_symptoms):
    # Define the dictionary called remedies.
    remedies = {
        "ignatia amara": {"acute", "depression", "constant", "sadness", "weeping" "spells", "isolation",
                          "deep" "thought", "irritability", "dull" "mind", "weak" "memory", "excessive" "weakness",
                          "acute" "grief", "broken", "relationships", "life", "disappointments", "bipolar", "disorder"},
        "natrum mur": {"sensitive", "individuals", "with", "sporadic", "episodes", "of", "weeping",
                       "suitable" "for" "those" "absorbed" "in" "grief", "dwelling" "on" "painful" "past" "memories",
                       "do" "not" "like" "consolation", "worsens" "complaints", "easy" "offender",
                       "lacks" "interest" "in" "work", "beneficial" "for" "managing" "depression", "in",
                       "women" "before" "menstruation"},
        "aurum met": {"extreme", "sadness", "and", "hopelessness", "constant", "suicidal", "thoughts", "feeling",
                      "worthless", "and", "of", "no", "value", "Negative", "thoughts", "dark", "future", "perception",
                      "life", "as", "a", "burden", "constant", "suicidal", "thoughts"},
        "kali phos": {"over-stressed", "anxious", "constant", "sadness", "negative", "thoughts", "reduce", "mental",
                      "and", "physical", "exhaustion", "anxiety", "attacks", "weeping", "spells", "and",
                      "sleeplessness"},
        "natrum sulph": {"overwhelming", "suicidal", "thoughts", "sadness", "weeping", "and", "irritability", "morning",
                         "sadness", "is", "most", "severe", "aversion", "to", "talking", "indifference", "towards",
                         "family", "frequent", "thoughts", "to", "end", "life", "confusion", "and", "difficulty", "in",
                         "thinking"},
        "sepia": {"menopause", "depression", "sadness", "aversion", "to", "family", "loss", "of", "interest", "in",
                  "work", "indifferent", "behavior", "towards", "life", "and", "family", "constant", "worry", "and",
                  "stress", "irritation", "and", "easy", "offending", "sporadic", "weeping", "spells", "seeking",
                  "consolation", "and", "sympathy", "loss", "of", "sexual", "desire", "depression", "triggered",
                  "after", "childbirth"},
        "cimicifuga racemosa": {"post-childhood", "depression", "known", "for", "treating", "extreme", "sadness", "and",
                                "darkness", "symptoms", "include", "exhaustion", "excessive", "talking", "indifferent",
                                "behavior", "fear", "of", "death", "and", "fear", "of", "mental", "insanity"},
        "lachesis": {"depression", "with", "delusion", "like", "psychotic", "depression", "sadness", "feelings", "of",
                     "abandonment", "excessive", "talkativeness", "delusions", "frequent", "switching", "of",
                     "subjects", "violent", "anger", "and", "madness", "delusions", "can", "cause", "suspicion", "and",
                     "fear", "of", "harm", "restlessness", "aversion", "to", "work", "and", "evasion", "from", "the",
                     "world"},
        "coffea crude": {"manages", "sleeplessness", "identifies", "constant", "thoughts", "leading", "to",
                         "sleeplessness", "manifests", "as", "nighttime", "restlessness", "with", "tossing", "and",
                         "turning", "mood", "changes", "irritability", "anxiety", "weeping", "and", "weakness"},
        "arsenic album": {"anxiety", "and", "sadness", "accompany", "sadness", "anxiety", "about", "health", "and",
                          "future", "intense", "restlessness", "marked", "weakness", "fears", "of", "disease",
                          "financial", "loss", "loneliness", "and", "death"}

    }

    # Let's iterate through the 'remedies' dictionary to find a match.
    for remedy, symptoms in remedies.items():
        if isinstance(symptoms, set):
            symptoms = ' '.join(symptoms)
        if signs_symptoms.lower() in symptoms.lower():
            return remedy

    # Let's return an error message if no match is found
    return "Remedy not found for the given signs and symptoms."


def get_remedy():
    # Let's get the signs and symptoms from the user input
    signs_symptoms = entry.get()

    # Let's find the remedy based on the signs and symptoms
    remedy = find_remedy(signs_symptoms)

    # Let's display the remedy in a message box
    messagebox.showinfo("Remedy", remedy)


# Let's create the main window
root = tk.Tk()
root.title("Medical Decision Support System")

# Let's create a label for the signs and symptoms
label = tk.Label(root, text="Enter signs and symptoms:")
label.pack()

# Let's create an entry field for the signs and symptoms
entry = tk.Entry(root)
entry.pack()

# Let's create a button to find the remedy
button = tk.Button(root, text="Find Remedy", command=get_remedy)
button.pack()

# Let's run the main event loop
root.mainloop()
