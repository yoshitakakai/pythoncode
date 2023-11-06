export default function StyleBasic() {
    return (
        <>
            <style jsx>{`
              :global(h3) {
                color: Red;
              }
               
            .panel {
              width: 300px;
              padding: 10px;
              border: 1px solid #000;
              border-radius: 5px;
              background-color: royalblue;
              color: white;
            }
            `}</style>
            <div className="panel"><b>Style JSX</b>は、JSX式にスタイル定義を埋め込む形式のライブラリです。</div>
        </>
    );
}