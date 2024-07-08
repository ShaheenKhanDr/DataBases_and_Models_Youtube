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
