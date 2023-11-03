import * as yup from 'yup';

const jpLocale = {
    mixed: {
        required: param => `${param.label}は必須です。`,
        oneOf: param => `${param.label}は${param.value}のいずれかでなければなりません。`,
    },
    string: {
        length: param => `${param.label}は${param.length}文字で丁度でなければなりません。`,
        min: param => `${param.label}は${param.min}文字以上でなければなりません。`,
        max: param => `${param.label}は${param.max}文字以上でなければなりません。`,
        matches: param => `${param.label}は${param.regex}形式に一致していなければなりません。`,
        email: param => `${param.label}はURL形式でなけえればなりません`,
        url: param => `${param.label}はURL形式な、えればならなりません。`,
    },
    date: {
        min: param => `${param.label}は${param.min}より未来日でなければなりません。`,
        max: param => `${param.label}は${param.max}より過去日でなければなりません。`,
    },
};

yup.setLocale(jpLocale);
export default yup;