def launch(*stages, abort_threshold=5000):

    total = 0

    for i in range(len(stages)):
        total += stages[i]

        print(f"Stage {i+1} armed -> cumulative {total} kg")

        if total > abort_threshold:
            print(f"[ABORT] at stage {i+1}: threshold {abort_threshold} kg exceeded.")
            return

    print(f"Launch successful!")
    print(f"Total mass: {total} kg")
    print(f"Stages fired: {len(stages)}")


launch(1200, 1800, 2500, 900)