# Finding the package
find_package(SFML 2.6.1 COMPONENTS system window graphics audio)

# Fetching the package if not found
if(NOT SFML_FOUND)
    include(FetchContent)

    FetchContent_Declare(
      SFML
      GIT_REPOSITORY "https://github.com/SFML/SFML"
      GIT_TAG 2.6.1
    )

    set(SFML_BUILD_NETWORK FALSE)

    message(STATUS "Fetching SFML...")
    FetchContent_MakeAvailable(SFML)
endif()