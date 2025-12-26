#!/usr/bin/env python3
"""
Main script to execute all metadata API operations
"""
import json

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
    # turn_on_tags_feature,
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

class MetadataAPITest:
    def __init__(self):
        self.start = 0
        self.limit = 5
        self.view_id = ""
        self.tag_id = ""

        self.new_column = "TestColumn"

        self.record_obj_id = ""
        self.record_id = ""
        self.record_parent_dir = ""
        self.record_file_name = ""

        self.people_id = ""

        try:
            response = get_metadata_enable_status()
            response_json = json.loads(response)
            if response_json.get("enabled") == False:
                enable_metadata()
            else:
                disable_metadata()
                enable_metadata()
        except Exception as e:
            print(f"Error in __init__ enable metadata: {e}")
        
        try:
            response = list_views()
            views_json = json.loads(response)
            self.view_id = views_json["navigation"][0]["_id"]
        except Exception as e:
            print(f"Error in __init__ list views: {e}")

        try:
            response = list_metadata_records(self.view_id, self.start, self.limit)
            records_json = json.loads(response)
            if len(records_json["results"]) == 0:
                print("No records found")
                return
            self.record_id = records_json["results"][0]["_id"]
            self.record_obj_id = records_json["results"][0]["_obj_id"]
            self.record_parent_dir = records_json["results"][0]["_parent_dir"]
            self.record_file_name = records_json["results"][0]["_name"]
        except Exception as e:
            print(f"Error in __init__ list metadata records: {e}")

        try:
            get_face_recognition_enabled_status()
            open_face_recognition()
            response = list_face_records(self.start, self.limit)
            face_records_json = json.loads(response)
            if len(face_records_json["results"]) == 0:
                print("No face records found")
            self.people_id = face_records_json["results"][0]["_id"]
        except Exception as e:
            print(f"Error in __init__ list face records: {e}")

        self._add_tag = { "tags_data": [
            {
                "_tag_name": "Tag1",
                "_tag_color": "#F4667C"
            },
            {
                "_tag_name": "Tag2",
                "_tag_color": "#36CD36"
            }
        ] }
        try:
            response = add_tags(self._add_tag)
            tags_json = json.loads(response)
            self.tag_id1 = tags_json["tags"][0]["_id"]
            self.tag_id2 = tags_json["tags"][1]["_id"]
        except Exception as e:
            print(f"Error in __init__ add tags: {e}")


        self.update_record = {
            "parent_dir": self.record_parent_dir,
            "file_name": self.record_file_name,
            "data": {
                "_description": "00000"
            }
        }
        self.update_records = {
            "records_data": [
                {
                    "record_id": self.record_id,
                    "_obj_id": self.record_obj_id,
                    "record": {
                        "_description": "11111",
                    }
                }
            ]
        }
        self._add_view = {
            "name": "New View",
        }
        self._update_tag = { "tags_data": [
            {
                "tag_id": self.tag_id1,
                "tag": {
                    "_tag_color": "#9860E5",
                    "_tag_name": "new tag"
                }
            }
        ] }
        self._update_file_tags = { "file_tags_data": [
            {
                "tags": [self.tag_id2],
                "record_id": self.record_id
            }
        ] }
        self._list_tags_files = { 
            "tags_ids": [self.tag_id1]
        }
        self._add_tags_links = {
            "row_id_map": { self.tag_id1 : [self.tag_id2] },
            "link_column_key": "_tag_parent_links"
        }
        self._delete_tags_links = {
            "link_column_key": "_tag_parent_links",
            "row_id_map": { self.tag_id1 : [self.tag_id2] }
        }
        self._merge_tags = {
            "merged_tags_ids": [self.tag_id2],
            "target_tag_id": self.tag_id1
        }
        self._delete_tags = ([
                self.tag_id1
        ])

        pass
    
    def run_config_api_tests(self):
        try:
            details_settings([self.new_column])
            exract_file_details([self.record_obj_id])
        except Exception as e:
            print(f"Error in run_config_api_tests: {e}")
        
    def run_records_api_tests(self):
        try:
            list_metadata_records(self.view_id, self.start, self.limit)
            get_metadata_record(self.record_parent_dir, self.record_file_name)
            update_metadata_record(self.update_record)
            update_metadata_records(self.update_records)
            add_column(self.new_column, self.new_column, "text")
        except Exception as e:
            print(f"Error in run_records_api_tests: {e}")

    def run_tags_api_tests(self):
        try:
            list_tags()
            update_tags(self._update_tag)
            update_file_tags(self._update_file_tags)
            list_tag_files(self.tag_id1)
            list_tags_files(self._list_tags_files)
            add_tags_links(self._add_tags_links)
            delete_tags_links(self._delete_tags_links)
            merge_tags(self._merge_tags)
            delete_tags(self._delete_tags)
            turn_off_tags_feature()
        except Exception as e:
            print(f"Error in run_tags_api_tests: {e}")

    def run_views_api_tests(self):
        try:
            response = add_view(self._add_view)
            views_json = json.loads(response)
            view_id1 = views_json["view"]["_id"]
            update_view(view_id1, "View1")
            get_a_view(view_id1)
            duplicate_view(view_id1)
            move_view(self.view_id, view_id1)
            delete_view(view_id1)
        except Exception as e:
            print(f"Error in run_views_api_tests: {e}") 

    def run_face_recognition_api_tests(self):
        pass
        # try:
        #     response = list_people_photos(self.people_id, self.start, self.limit)
        #     photos_json = json.loads(response)
        #     photo_rocord_id = photos_json["results"][0]["_id"]
        #     remove_people_photos(self.people_id, { "record_ids": [photo_rocord_id] })
        #     update_people_cover_photo(self.people_id, { "record_id": photo_rocord_id })
        # except Exception as e:
        #     print(f"Error in run_face_recognition_api_tests: {e}")   
def main():
    metadata_test = MetadataAPITest()
    metadata_test.run_config_api_tests()
    metadata_test.run_records_api_tests()
    metadata_test.run_views_api_tests()
    metadata_test.run_tags_api_tests()
    metadata_test.run_face_recognition_api_tests()

    print("\n========== All tests completed ==========")


if __name__ == "__main__":
    main()
