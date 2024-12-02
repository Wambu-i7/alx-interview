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

// Make an HTTP GET request to fetch the movie details
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode}`);
    return;
  }

  const filmData = JSON.parse(body);

  // Fetch and print each character's name in order
  const characters = filmData.characters;
  const fetchCharacterName = (url) => {
    return new Promise((resolve, reject) => {
      request(url, (err, res, data) => {
        if (err) reject(err);
        if (res.statusCode === 200) {
          const character = JSON.parse(data);
          resolve(character.name);
        } else {
          reject(`Failed to fetch ${url}`);
        }
      });
    });
  };

  // Fetch names sequentially
  (async () => {
    for (const characterUrl of characters) {
      try {
        const name = await fetchCharacterName(characterUrl);
        console.log(name);
      } catch (err) {
        console.error(err);
      }
    }
  })();
});

