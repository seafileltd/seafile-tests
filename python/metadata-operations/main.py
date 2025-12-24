#!/usr/bin/env python3
"""
Main script to execute all metadata API operations
"""

import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# Import all API modules
from apis.config_api import (
    get_metadata_enable_status,
    enable_metadata,
    disable_metadata,
    details_settings,
    exract_file_details
)

from apis.face_recognition_api import (
    get_face_recognition_enabled_status,
    open_face_recognition,
    list_face_records,
    list_people_photos,
    remove_people_photos,
    update_people_cover_photo
)

from apis.records_api import (
    list_metadata_records,
    update_metadata_records,
    get_metadata_record,
    update_metadata_record,
    add_column
)

from apis.tags_api import (
    turn_off_tags_feature,
    list_tags,
    add_tags,
    update_tags,
    delete_tags,
    update_file_tags,
    list_tag_files,
    list_tags_files,
    add_tags_links,
    delete_tags_links,
    merge_tags
)

from apis.views_api import (
    list_views,
    add_view,
    update_view,
    delete_view,
    get_a_view,
    move_view,
    duplicate_view
)


def run_config_api_tests():
    try:
        get_metadata_enable_status()
    except Exception as e:
        print(f"Error in get_metadata_enable_status: {e}")
    
    try:
        enable_metadata()
    except Exception as e:
        print(f"Error in enable_metadata: {e}")
    
    try:
        disable_metadata()
    except Exception as e:
        print(f"Error in disable_metadata: {e}")
    
    try:
        details_settings(["testColumn"])
    except Exception as e:
        print(f"Error in details_settings: {e}")
    
    try:
        exract_file_details(["ad60423a854bc14ad7aa2d82c79bfbb9c7753478"])
    except Exception as e:
        print(f"Error in exract_file_details: {e}")


def run_face_recognition_api_tests():
    try:
        get_face_recognition_enabled_status()
    except Exception as e:
        print(f"Error in get_face_recognition_enabled_status: {e}")
    
    try:
        open_face_recognition()
    except Exception as e:
        print(f"Error in open_face_recognition: {e}")
    
    try:
        list_face_records(0,5)
    except Exception as e:
        print(f"Error in list_face_records: {e}")
    
    try:
        list_people_photos("LZQ_sH2lTguOCKR76Gmm4w", 0, 5)
    except Exception as e:
        print(f"Error in list_people_photos: {e}")
    
    try:
        remove_people_photos("LZQ_sH2lTguOCKR76Gmm4w", { "record_ids": ["wQAzg1GAQV6-FWmKmUNqgw"] })
    except Exception as e:
        print(f"Error in remove_people_photos: {e}")
    
    try:
        update_people_cover_photo("LZQ_sH2lTguOCKR76Gmm4w", { "record_id": "l52n-YEsReqIovE8F1_bHw" })
    except Exception as e:
        print(f"Error in update_people_cover_photo: {e}")


def run_records_api_tests():
    try:
        list_metadata_records("hbqp", 0, 10)
    except Exception as e:
        print(f"Error in list_metadata_records: {e}")
    
    try:
        get_metadata_record("/", "test.sdoc")
    except Exception as e:
        print(f"Error in get_metadata_record: {e}")
    
    try:
        update_metadata_record("/", "test.sdoc", {"_description": "18888"})
    except Exception as e:
        print(f"Error in update_metadata_record: {e}")
    
    try:
        update_metadata_records( {
        "records_data": [
            {
                "record_id": "n9vyqgI4SRugwJ-yLxKTWw",
                "_obj_id": "f876cec256027ded8710441e49f33eac61515c59",
                "record": {
                    "_description": "00000",
                }
            }
        ]
    })
    except Exception as e:
        print(f"Error in update_metadata_records: {e}")
    
    try:
        add_column("testColumn1", "testColumn1", "text")
    except Exception as e:
        print(f"Error in add_column: {e}")


def run_tags_api_tests():
    try:
        list_tags()
    except Exception as e:
        print(f"Error in list_tags: {e}")
    
    try:
        add_tags([
        {
            "_tag_name": "tagTest2",
            "_tag_color": "#F4667C"
        }
    ])
    except Exception as e:
        print(f"Error in add_tags: {e}")
    
    try:
        update_tags([
        {
            "tag_id": "AcqwwxjeQHeTeo1ExpPZbg",
            "tag": {
                "_tag_color": "#9860E5",
                "_tag_name": "newTagTest"
            }
        }
    ])
    except Exception as e:
        print(f"Error in update_tags: {e}")
    
    try:
        delete_tags([
        "AcqwwxjeQHeTeo1ExpPZbg"
    ])
    except Exception as e:
        print(f"Error in delete_tags: {e}")
    
    try:
        update_file_tags({ 
        "file_tags_data": [
        {
            "tags": ["gXe6D6XhQmSmst5SizjAWQ",
                     "CzRlYMm1SiWrBiHHu5KH8Q"],
            "record_id": "-P52LX7KRPGO_lo273YEYg"
        }
        ]
    })
    except Exception as e:
        print(f"Error in update_file_tags: {e}")
    
    try:
        list_tag_files("gXe6D6XhQmSmst5SizjAWQ")
    except Exception as e:
        print(f"Error in list_tag_files: {e}")
    
    try:
        list_tags_files({ 
        "tags_ids": ["gXe6D6XhQmSmst5SizjAWQ", "CzRlYMm1SiWrBiHHu5KH8Q"]
    })
    except Exception as e:
        print(f"Error in list_tags_files: {e}")
    
    try:
        add_tags_links({
        "row_id_map": { "gXe6D6XhQmSmst5SizjAWQ": ["CzRlYMm1SiWrBiHHu5KH8Q"] },
        "link_column_key": "_tag_parent_links"
    })
    except Exception as e:
        print(f"Error in add_tags_links: {e}")
    
    try:
        delete_tags_links({
        "link_column_key": "_tag_parent_links",
        "row_id_map": { "gXe6D6XhQmSmst5SizjAWQ": ["CzRlYMm1SiWrBiHHu5KH8Q"] }
    })
    except Exception as e:
        print(f"Error in delete_tags_links: {e}")
    
    try:
        merge_tags({
        "merged_tags_ids": ["gXe6D6XhQmSmst5SizjAWQ"],
        "target_tag_id": "CzRlYMm1SiWrBiHHu5KH8Q"
    })
    except Exception as e:
        print(f"Error in merge_tags: {e}")

    
    try:
        turn_off_tags_feature()
    except Exception as e:
        print(f"Error in turn_off_tags_feature: {e}")

def run_views_api_tests():
    try:
        list_views()
    except Exception as e:
        print(f"Error in list_views: {e}")
    
    try:
        add_view(_name="New View")
    except Exception as e:
        print(f"Error in add_view: {e}")
    
    try:
        update_view("4jmf", "NewViewName")
    except Exception as e:
        print(f"Error in update_view: {e}")
    
    try:
        delete_view("4jmf")
    except Exception as e:
        print(f"Error in delete_view: {e}")
        
    try:
        get_a_view("f72b")
    except Exception as e:
        print(f"Error in get_a_view: {e}")
    
    try:
        move_view("zb6q", "f72b")
    except Exception as e:
        print(f"Error in move_view: {e}")
    
    try:
        duplicate_view("f72b")
    except Exception as e:
        print(f"Error in duplicate_view: {e}")


def main():
    run_config_api_tests()
    run_face_recognition_api_tests()
    run_records_api_tests()
    run_tags_api_tests()
    run_views_api_tests()

    print("\n========== All tests completed ==========")


if __name__ == "__main__":
    main()
