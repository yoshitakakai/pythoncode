import React from "react";
import Star from "./Star";
import PropTypes from "prop-types";

const StarRating = ({ totalStars = 5, selectedStars = 0, onRate }) => {
    return (
        <>
            {[...Array(totalStars)].map((_, i) => (
                <Star
                    key={i}
                    selected={selectedStars > i}
                    onSelect={() => onRate(i + 1)}
                />
            ))}
        </>
    );
};

StarRating.propTypes = {
    totalStars: PropTypes.number,
    selectedStars: PropTypes.number,
    onRate: PropTypes.func.isRequired,
};

export default StarRating;