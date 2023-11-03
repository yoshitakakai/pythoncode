import PropTypes from "prop-types";

export function Member() {}
    function TypeProp(props) {
        console.log(props);
        return <p>コンソールを確認</p>
    }

    TypeProp.propTypes = {
        prop1: PropTypes.instanceOf(Member),
        prop2: PropTypes.oneOf(['男', '女', 'その他']),
        prop3: PropTypes.oneOfType([
            PropTypes.string,
            PropTypes.number,
            PropTypes.bool,
        ]),
        prop6: PropTypes.shape({
            name: PropTypes.string.isRequired,
            age: PropTypes.number,
            sex: PropTypes.oneOf(['男', '女', 'その他']),
        })
    };

export default TypeProp;