#!/usr/bin/node

const request = require('request');

// Get the movie ID from command line arguments
const movieID = process.argv[2];
if (!movieID) {
    console.log('Please provide a movie ID as the first argument.');
    process.exit(1);
}

// Define the Star Wars API endpoint for the specified movie ID
const apiEndpoint = `https://swapi.dev/api/films/${movieID}/`;

// Make a request to the API endpoint
request(apiEndpoint, (error, response, body) => {
    if (error) {
        console.error('Error fetching data from the API:', error);
        return;
    }

    // Parse the JSON response
    const data = JSON.parse(body);

    // Check if the API returned an error
    if (!data || data.detail === 'Not found') {
        console.log('Movie not found.');
        return;
    }

    // Get the list of character URLs
    const characters = data.characters;

    // Fetch and print each character's name in order
    characters.forEach((characterURL) => {
        request(characterURL, (error, response, body) => {
            if (error) {
                console.error('Error fetching character data:', error);
                return;
            }

            // Parse the JSON response
            const characterData = JSON.parse(body);

            // Print the character's name
            console.log(characterData.name);
        });
    });
});
#!/usr/bin/node

const request = require('request');

// Get the movie ID from command line arguments
const movieID = process.argv[2];
if (!movieID) {
    console.log('Please provide a movie ID as the first argument.');
    process.exit(1);
}

// Define the Star Wars API endpoint for the specified movie ID
const apiEndpoint = `https://swapi.dev/api/films/${movieID}/`;

// Make a request to the API endpoint
request(apiEndpoint, (error, response, body) => {
    if (error) {
        console.error('Error fetching data from the API:', error);
        return;
    }

    // Parse the JSON response
    const data = JSON.parse(body);

    // Check if the API returned an error
    if (!data || data.detail === 'Not found') {
        console.log('Movie not found.');
        return;
    }

    // Get the list of character URLs
    const characters = data.characters;

    // Fetch and print each character's name in order
    characters.forEach((characterURL) => {
        request(characterURL, (error, response, body) => {
            if (error) {
                console.error('Error fetching character data:', error);
                return;
            }

            // Parse the JSON response
            const characterData = JSON.parse(body);

            // Print the character's name
            console.log(characterData.name);
        });
    });
});

