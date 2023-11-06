/** @jsxImportSource @emotion/react */
import { css } from '@emotion/react';
import { Button } from '@mui/material';

export default function MaterialBasic() {
    const font = css`
    text-transform: none;
    `;
    return (
        <>
            <Button variant="text" css={font} color="secondary">Text</Button>
            <Button variant="contained" css={font} color="secondary">Contained</Button>
            <Button variant="outlined" css={font} color="secondary">Outlined</Button>
        </>
    );
}