cmake_minimum_required(VERSION 3.15)
project(build)
find_package(SFML 2.6.1 COMPONENTS system window graphics audio)

if(NOT SFML_FOUND)
    include(FetchContent)

    FetchContent_Declare(
      SFML
      GIT_REPOSITORY "https://github.com/SFML/SFML"
      GIT_TAG 2.6.1
    )

    message(STATUS "Fetching SFML...")
    FetchContent_MakeAvailable(SFML)
else ()
    message(STATUS "SFML 2.6.1 is already installed.")
endif()