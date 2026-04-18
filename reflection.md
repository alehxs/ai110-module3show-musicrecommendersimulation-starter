# Reflection: Profile Comparisons

## Pop Fan vs. Lofi Studier

Both have genres that exist in the catalog, but Lofi Studier gets a perfect 5.0 while Pop Fan tops out at 4.46 with no mood matches in the top 4. The difference is that lofi songs in this dataset cluster tightly in mood and energy, while happy pop songs are spread all over the energy scale.

## Pop Fan vs. Hype Workout

Pop Fan gets a coherent genre-anchored list; Hype Workout gets reggaeton, rock, salsa, and regional mexican all mixed together. The reason is that "edm" does not exist in the catalog, so Hype Workout earns zero genre points on every song and the ranking falls back to energy alone.

## Lofi Studier vs. Acoustic Lover (folk, relaxed, 0.3)

Both want calm low-energy music but land in totally different parts of the catalog. The "chill" vs. "relaxed" mood distinction is enough to route them into separate sonic spaces, which shows the mood signal is doing real work even when energy levels are nearly the same.

## Mood-that-doesn't-exist (sad+pop+0.9) vs. Energy-mood contradiction (intense+lofi+0.9)

Both profiles ask for something the catalog cannot actually deliver. The sad+pop list looks tidy because genre dominates and produces a clean pop list. The intense+lofi list looks scattered because the genre and mood pull in different directions. In both cases the system returns confident results while completely ignoring what the user actually asked for.

## k=-1 slice bug vs. any normal profile

A normal k=5 run returns 5 songs. With k=-1, Python's list slicing returns 19 songs with no error. The system silently does something unexpected instead of failing clearly. Any real app would need to validate k before it ever reaches the slice.
