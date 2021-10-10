import React from "react";
import { AbstractReactFactory, AbstractModelFactory } from '@projectstorm/react-canvas-core';
import { DefaultLinkModel } from "@projectstorm/react-diagrams";
import { PortModel, PortModelAlignment, NodeModel, PortWidget, DefaultPortModel } from "@projectstorm/react-diagrams";
import styles from './index.module.css';


export class VariablePortModel extends DefaultPortModel {
	constructor(alignment, isIn) {
		super({
            in: isIn,
			type: 'variable',
			name: alignment,
			alignment: alignment,
		});
	}

    createLinkModel() {
		return new DefaultLinkModel();
	}
}


export class VariablePortFactory extends AbstractModelFactory {
	cb;

	constructor(type, cb) {
		super(type);
		this.cb = cb;
	}

	generateModel(event) {
		return this.cb(event.initialConfig);
	}
}


export class VariableNodeModel extends NodeModel {
    value = ''

    constructor() {
        super({
            type: 'variable',
            name: 'variable'
        });
        this.addPort(new VariablePortModel(PortModelAlignment.RIGHT, false));
        this.addPort(new VariablePortModel(PortModelAlignment.LEFT, true));
    }

    serialize() {
        console.log(this.value);
        return {
            ...super.serialize(),
            value: this.value,
        };
    }
}

export class VariableNodeWidget extends React.Component {
    constructor(props) {
        super(props);
        this.handleChange = this.handleChange.bind(this);
    }

    handleChange(e) {
        this.props.node.value = e.target.value;
    }

    render() {
        return (
            <div className={styles.variableNode}>
                <input type="text"  className={styles.variableInput} onChange={this.handleChange}/>
                <PortWidget className={styles.variablePort}
                    port={this.props.node.getPort(PortModelAlignment.RIGHT)}
                    engine={this.props.engine} />
                <PortWidget className={styles.variablePort}
                    port={this.props.node.getPort(PortModelAlignment.LEFT)}
                    engine={this.props.engine} />
            </div>
        );
    }
}

export class VariableNodeFactory extends AbstractReactFactory {
    constructor() {
        super('variable');
    }

    generateReactWidget(event) {
        // event.model is basically what's returned from generateModel()
        return <VariableNodeWidget engine={this.engine} size={50} node={event.model} />;
    }

    generateModel(event) {
        return new VariableNodeModel();
    }
}
