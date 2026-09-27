mismatches = [

    item for item in batch

    if item["predicted_label"] != item["human_label"]

    ]

print([item["image_id"] for item in mismatches])

print(len(mismatches))
