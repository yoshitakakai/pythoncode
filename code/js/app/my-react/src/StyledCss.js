import css, { globalCss, resolveCss } from './StyledComp';

export default function StyledCss() {
    return (
        <>
            <style jsx>{css}</style>
            <style jsx>{globalCss}</style>
            {resolveCss.styles}
            <div className={`panel ${resolveCss.className}`}>
                <b>Styled JSX</b>は、JSX式にスタイル定義を埋め込む形式のライブラリです。
            </div>
        </>
    );
}