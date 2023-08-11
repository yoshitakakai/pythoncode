import React, {Component} from 'react';

export default class MultiForm extends Component {
    constructor(props) {
        super(props)
        this.state = {
            name: '名前を入力',
            age: '年齢を入力',
            hobby: '趣味を入力'
        }
    }
    doChange (e) {
        const userValue = e.target.value
        const key = e.target.name
        this.setState({[key]: userValue})
    }
    doSubmit (e) {
        e.preventDefault()
        const j = JSON.stringify(this.state)
        window.alert(j)
    }
    render () {
        const doSubmit = (e) => this.doSubmit(e)
        const doChange = (e) => this.doChange(e)
        return (
            <form onSubmit={doSubmit}>
                <div>
                    <label>
                        名前: <br />
                        <input
                            name='name'
                            type='text'
                            value={this.state.name}
                            onChange={doChange}
                        />
                    </label>
                </div>
                <div>
                    <label>
                        年齢: <br />
                        <input
                            name='age'
                            type='text'
                            value={this.state.age}
                            onChange={doChange}
                        />
                    </label>
                </div>
                <div>
                    <label>
                        趣味: <br />
                        <input
                            name='hobby'
                            type='text'
                            value={this.state.hobby}
                            onChange={doChange}
                        />
                    </label>
                </div>
                <input type='submit' value='送信' />
            </form>
        )
    }
}