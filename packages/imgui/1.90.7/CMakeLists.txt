cmake_minimum_required(VERSION 3.15)
project(build)
find_package(imgui 1.90.7)

if(NOT imgui_FOUND)
    include(FetchContent)

    FetchContent_Declare(
        imgui
        GIT_REPOSITORY https://github.com/ocornut/imgui
        GIT_TAG v1.90.7
      )

    message(STATUS "Fetching ImGui...")
    FetchContent_MakeAvailable(imgui)
else ()
    message(STATUS "ImGui 1.90.7 is already installed.")
endif()