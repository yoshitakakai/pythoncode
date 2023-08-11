import React, {Component} from 'react';

export default class ValueInput extends Component {
    constructor(props) {
        super(props)
        this.state = {
            value: this.props.value
        }
    }
    handleChange(e) {
  const newValue = e.target.value;
  const filteredValue = newValue.replace(/[^0-9.]+/g, '');

  this.setState({ value: filteredValue });

  if (this.props.onChange) {
    this.props.onChange({
      target: this,
      value: filteredValue
    });
  }
}
    componentDidUpdate(prevProps) {
    if (prevProps.value !== this.props.value) {
        this.setState({ value: this.props.value });
    }
}
    render () {
        return (
            <div>
                <label>
                    {this.props.title}: <br />
                    <input type='text'
                           value={this.state.value}
                           onChange={e => this.handleChange(e)} />
                </label>
            </div>
        )
    }
}