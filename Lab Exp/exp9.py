activity = input("Describe the intelligence activity: ").lower()

stages = {
    "Direction": ["define requirements", "set objectives", "priorities", "intelligence needs"],
    "Collection": ["gather logs", "collect data", "threat feeds", "collect evidence"],
    "Processing": ["normalize", "clean data", "parse logs", "deduplicate"],
    "Analysis": ["investigate", "correlate", "interpret", "assess threat"],
    "Dissemination": ["share report", "publish", "send findings", "distribute"],
    "Feedback": ["feedback", "review usefulness", "improve process", "request feedback"]
}

matches = [stage for stage, keywords in stages.items()
           if any(keyword in activity for keyword in keywords)]

if matches:
    print("Lifecycle Stage:", matches[0])
else:
    print("Stage could not be identified")
