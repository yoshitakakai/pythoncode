import React from 'react';

export default function ForList({ src, children }) {

    return (
        <dl>
            {
                src.map(elem => (
                    <React.Fragment key={elem.isbn}>
                        {children(elem)}
                    </React.Fragment>
                ))}
        </dl>
    );
}


