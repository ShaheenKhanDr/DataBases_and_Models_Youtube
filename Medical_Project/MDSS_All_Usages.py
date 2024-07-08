# Python Medical Project to Find_Remedy
# By the Name of "Medical Decision Support System_MDSS"

# Let's define a function that takes a single argument 'signs_symptoms' to represents the signs of a patient.
def find_remedy(signs_symptoms):

    # Let's compile a dictionary called 'remedies' to carry the remedy names as keys and their corresponding sign & symptoms as values.
    remedies = {
        "ignatia amara": "acute depression, constant sadness, weeping spells, isolation, deep thought, irritability, dull mind, weak memory, excessive weakness, acute grief, broken relationships, life disappointments, bipolar disorder",
        "natrum mur": "sensitive individuals with sporadic episodes of weeping, suitable for those absorbed in grief, dwelling on painful past memories, do not like consolation, worsens complaints, easy offender, lacks interest in work, beneficial for managing depression in women before menstruation",
        "aurum met": "extreme hopelessness, feeling worthless and of no value, Negative thoughts, dark future perception, life as a burden, constant suicidal thoughts",
        "kali phos": "over-stressed and anxious, constant sadness and negative thoughts reduce mental and physical exhaustion, anxiety attacks, weeping spells, and sleeplessness",
        "natrum sulph": "overwhelming suicidal thoughts, sadness, weeping, and irritability, morning sadness is most severe, aversion to talking, indifference towards family, frequent thoughts to end life, confusion and difficulty in thinking",
        "sepia": "menopause depression, sadness, aversion to family, loss of interest in work, indifferent behavior towards life and family, constant worry and stress, irritation and easy offending, sporadic weeping spells seeking consolation and sympathy, loss of sexual desire, depression triggered after childbirth",
        "cimicifuga racemosa": "post-childhood depression, known for treating extreme sadness and darkness, symptoms include exhaustion, excessive talking, indifferent behavior, fear of death, and fear of mental insanity",
        "lachesis": "depression with delusion, like psychotic depression, sadness, feelings of abandonment, excessive talkativeness, delusions, frequent switching of subjects, violent anger, and madness, delusions can cause suspicion and fear of harm, restlessness, aversion to work, and evasion from the world",
        "coffea crude": "manages sleeplessness, identifies constant thoughts leading to sleeplessness, manifests as nighttime restlessness with tossing and turning, mood changes, irritability, anxiety, weeping, and weakness",
        "arsenic album": "anxiety and sadness accompany sadness, anxiety about health and future, intense restlessness, marked weakness, fears of disease, financial loss, loneliness, and death"
    }

# Let's initiate a loop that iterates through each key-value pair in the dictionary.
    for remedy, symptoms in remedies.items():
        # Let's check matching symptoms within the loop, if the input signs_symptoms (converted to lowercase) are present in the symptoms string associated with the current remedy.
        # Make sure the lower() method comparison is case-insensitive.
        if signs_symptoms.lower() in symptoms.lower():

            # Let's return the remedy if a match is found.
            return remedy
        # Let's handle no match, if no match is found after iterating through all remedies, return an error message.
    return "Remedy not found for the given signs and symptoms."


# Let's define the main function to reach to the entry point of the program
def main():

    # Let's take user's input.
    signs_symptoms = input("Enter the patient's signs and symptoms:")

    # Let's call the find_remedy Function.
    remedy = find_remedy(signs_symptoms)

    # Let's print the result.
    print("Remedy:", remedy)


# Let's execute the main function.
if __name__ == "__main__":
    main()


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


# LET'S SELECT THE BEST REMEDY
def find_best_remedy(signs_symptoms):
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

    # Let's initialize an empty list to store remedies that match the symptoms
    matching_remedies = []

    # Let's iterate over each remedy and its symptoms
    for remedy, symptoms in remedies.items():

        # Let's check if the symptoms are stored as a set
        if isinstance(symptoms, set):

            # Let's convert the set to a string for easier comparison
            symptoms = ' '.join(symptoms)

            # Let's check if the input signs and symptoms match any remedy
        if signs_symptoms.lower() in symptoms.lower():
            # Let's add the matching remedy to the list
            matching_remedies.append(remedy)

    # If no remedies match the input signs and symptoms
    if not matching_remedies:
        return "Remedy not found for the given signs and symptoms."

    # Choose the best remedy based on some criteria (e.g., most specific or most effective)
    best_remedy = max(matching_remedies, key=lambda x: len(remedies[x]))

    # Return the best remedy found
    return best_remedy


# Get user input for signs and symptoms
signs_symptoms = input("Enter signs and symptoms of the Patients:")

# Find the best remedy based on the input
best_remedy = find_best_remedy(signs_symptoms)

# Print the best remedy found
print("Best Remedy:", best_remedy)
