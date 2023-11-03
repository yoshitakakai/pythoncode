import './EventPropagation.css';
export default function EventPropagation() {
    const handleParent = () => alert('#parent run...');
    const handleMy = () => alert('#my run...');
    const handleChild = e => {
        e.preventDefault();
        alert('#child run...');
    };

    return (
        <div id="parent" onClick={handleParent}>
            <div id="my" onClick={handleMy}>
                現在要素
                <a id="child" href="https://wings.msn.to" onClick={handleChild}>
                    子要素
                </a>
            </div>
        </div>
    );
}