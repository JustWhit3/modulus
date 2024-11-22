# create_json_file
function(create_json_file output_path condition version)
    set(JSON_FILE_CONTENT "{\n  \"found\": \"${condition}\",\n  \"version\": \"${version}\"\n}")
    set(JSON_FILE_PATH ${output_path})
    file(WRITE ${JSON_FILE_PATH} "${JSON_FILE_CONTENT}")
    message(STATUS "JSON file created: ${JSON_FILE_PATH}")
endfunction()