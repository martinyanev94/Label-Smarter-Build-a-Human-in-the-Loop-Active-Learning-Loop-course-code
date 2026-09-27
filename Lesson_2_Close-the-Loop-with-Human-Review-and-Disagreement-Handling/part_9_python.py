accepted_training = [

    item for item in batch

    if item.get("review_status") == "accepted"

    ]

review_queue = [

    item for item in batch

    if item.get("review_status") != "accepted"

    ]

remaining_pool = ["pkg_101", "pkg_102", "pkg_103", "pkg_104"]

accepted_ids = {item["image_id"] for item in accepted_training}

remaining_pool = [

    image_id for image_id in remaining_pool

    if image_id not in accepted_ids

    ]

print([item["image_id"] for item in accepted_training])

print([item["image_id"] for item in review_queue])

print(remaining_pool)
