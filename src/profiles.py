EDGE_PROFILES = [
    {
        "label": "1. Mood-that-doesn't-exist (sad+pop+0.9)",
        "prefs": {"genre": "pop", "mood": "sad", "energy": 0.9},
        "k": 5,
    },
    {
        "label": "2. Energy-mood contradiction (intense lofi+0.9)",
        "prefs": {"genre": "lofi", "mood": "intense", "energy": 0.9},
        "k": 5,
    },
    {
        "label": "3. k=-1 slice bug",
        "prefs": {"genre": "pop", "mood": "happy", "energy": 0.5},
        "k": -1,
    },
    {
        "label": "4. Acoustic lover ignored (folk+relaxed+0.3)",
        "prefs": {"genre": "folk", "mood": "relaxed", "energy": 0.3},
        "k": 5,
    },
    {
        "label": "5. Tie-breaking (synthwave+happy+0.79)",
        "prefs": {"genre": "synthwave", "mood": "happy", "energy": 0.79},
        "k": 5,
    },
]
