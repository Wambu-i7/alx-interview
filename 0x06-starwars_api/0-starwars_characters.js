#!/usr/bin/node

const request = require('request');

// Get the Movie ID from command-line arguments
const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

// Star Wars API endpoint for the specified movie
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Fetch movie details
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching movie details:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Received status code ${response.statusCode}`);
    return;
  }

  try {
    const filmData = JSON.parse(body);
    const characters = filmData.characters;

    // Fetch all character names in parallel
    const characterPromises = characters.map((url) => {
      return new Promise((resolve, reject) => {
        request(url, (err, res, data) => {
          if (err) {
            reject(new Error(`Error fetching character data: ${err}`));
            return;
          }

          if (res.statusCode === 200) {
            try {
              const character = JSON.parse(data);
              resolve(character.name);
            } catch (parseError) {
              reject(new Error(`Error parsing character data: ${parseError}`));
            }
          } else {
            reject(new Error(`Failed to fetch ${url}. Status code: ${res.statusCode}`));
          }
        });
      });
    });

    // Resolve all promises and print names in order
    Promise.all(characterPromises)
      .then((names) => {
        names.forEach((name) => console.log(name));
      })
      .catch((err) => {
        console.error('Error fetching character names:', err);
      });
  } catch (parseError) {
    console.error('Error parsing movie data:', parseError);
  }
});
