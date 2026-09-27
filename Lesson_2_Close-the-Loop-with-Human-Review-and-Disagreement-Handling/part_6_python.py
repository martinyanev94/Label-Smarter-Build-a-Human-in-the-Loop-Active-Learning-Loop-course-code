mismatches[0].update({

    "reviewed_label": "tube",

    "review_reason": "poor image quality; reviewer confirms tube",

    "review_status": "accepted",

    "status": "accepted",

})

for item in batch:

    if item.get("review_status") == "accepted":

        item["training_label"] = item.get(

            "reviewed_label", item["human_label"]

        )
