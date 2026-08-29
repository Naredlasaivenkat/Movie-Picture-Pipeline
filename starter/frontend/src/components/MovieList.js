import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';

function MovieList({ onMovieClick }) {
  const [movies, setMovies] = useState([]);
  const [error, setError] = useState('');

  useEffect(() => {
    axios
      .get(`${process.env.REACT_APP_MOVIE_API_URL}/movies`)
      .then((response) => {
        console.log('Movie API response:', response.data);

        if (Array.isArray(response.data.movies)) {
          setMovies(response.data.movies);
        } else {
          setMovies([]);
          setError('Invalid movie data received from server');
        }
      })
      .catch((err) => {
        console.error('Movie API error:', err);
        setMovies([]);
        setError('Unable to load movies');
      });
  }, []);

  if (error) {
    return <p>{error}</p>;
  }

  return (
    <ul>
      {movies.map((movie) => (
        <li className="movieItem" key={movie.id} onClick={() => onMovieClick(movie)}>
          {movie.title}
        </li>
      ))}
    </ul>
  );
}

MovieList.propTypes = {
  onMovieClick: PropTypes.func.isRequired,
};

export default MovieList;