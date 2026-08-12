

def launch(*stages, abort_threshold=5000):
    total = 0
    stage_number = 1

    for mass in stages:
        total = total + mass

        print("Stage", stage_number, "armed > cumulative", total, "kg")

        if total > abort_threshold:
            print("[ABORT] at stage", stage_number, ": threshold", abort_threshold, "kg exceeded.")
            return

        stage_number = stage_number + 1

    print("Total mass:", total, "kg")
    print("Stage count:", len(stages))


launch(1200, 1800, 2500, 900)