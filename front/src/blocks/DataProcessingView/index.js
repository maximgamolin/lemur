import React from "react";
import createEngine, {
    DefaultLinkModel,
    DefaultNodeModel,
    DiagramModel,
    PortModelAlignment,
} from '@projectstorm/react-diagrams';
import Dropdown from 'react-bootstrap/Dropdown';
import Button from 'react-bootstrap/Button';
import { CanvasWidget } from '@projectstorm/react-canvas-core';
import { useEffect, useState } from "react";
import 'bootstrap/dist/css/bootstrap.min.css';

import styles from './index.module.css';
import CustomState from "./CustomState";
import { VariableNodeFactory, VariableNodeModel, VariablePortFactory, VariablePortModel } from './VariableNode';


function useForceUpdate() {
    const [value, setValue] = useState(0);
    return () => setValue(value => value + 1);
}

function DataProcessingView({ onChange, className, datasets, operators, addResBlock, ...rest }) {
    const [engine, setEngine] = useState();
    const [model, setModel] = useState();
    const forceUpdate = useForceUpdate();

    useEffect(() => {
        const engine = createEngine();

        const model = new DiagramModel();
        let y_counter = 100;
        for (const dataset of datasets) {
            const node = new DefaultNodeModel({
                name: dataset.name,
                color: 'rgb(0,192,255)',
            });

            if (dataset.fields) {
                for (const field of dataset.fields) {
                    node.addOutPort(field.name);
                }
            }

            node.setPosition(100, y_counter);
            y_counter += 100;

            model.addNode(node);
        }

        if (addResBlock) {
            const node = new DefaultNodeModel({
                name: 'res',
                color: 'rgb(0,192,255)',
            });
            node.addInPort('res');
            node.setPosition(500, 100);
            model.addNode(node);
        }

        engine.getPortFactories().registerFactory(
            new VariablePortFactory('variable', (config) => new VariablePortModel(PortModelAlignment.LEFT))
        );
        engine.setModel(model);
        // engine.getStateMachine().pushState(new CustomState());
        engine.getNodeFactories().registerFactory(new VariableNodeFactory());

        setModel(model);
        setEngine(engine);
    }, [datasets]);

    function addOperator(id) {
        const operator = operators.find((item) => item.id === id);
        if (!operator)
            return;

        const node = new DefaultNodeModel({
            name: operator.title,
            color: 'rgb(0,192,255)',
        });
        for (const port of operator.inPorts)
            node.addInPort(port);
        for (const port of operator.outPorts)
            node.addOutPort(port);

        node.setPosition(200, 200);
        model.addNode(node);
        forceUpdate();
    }

    function addVariable() {
        const var1 = new VariableNodeModel({
            name: 'v1',
        });
        var1.setPosition(300, 300);
        model.addNode(var1);
        forceUpdate();
    }

    function dump() {
        const res = {};

        let nodes, links;
        for (const layer of model.serialize().layers) {
            if (layer.type === 'diagram-links')
                links = layer;
            else if (layer.type === 'diagram-nodes')
                nodes = layer;
        }

        res['nodes'] = Object.keys(nodes.models).map((id) => ({
            id: id,
            name: nodes.models[id].name,
            value: nodes.models[id].value,
            ports: nodes.models[id].ports.map((port) => ({
                id: port.id,
                name: port.name,
            })),
        }));
        res['links'] = Object.keys(nodes.models).map((id) => ({
            id: id,
            source: nodes.models[id].source,
            sourcePort: nodes.models[id].sourcePort,
            target: nodes.models[id].target,
            targetPort: nodes.models[id].targetPort,
        }));

        onChange(res);
    }

    const groupedOperators = {};
    for (const operator of operators)
        if (operator.category in groupedOperators)
            groupedOperators[operator.category].push(operator);
        else
            groupedOperators[operator.category] = [operator];

    return (
        <div onClick={dump} className={styles.wrapper} {...rest} >
            <div className={styles.toolsMenu}>
                {Object.keys(groupedOperators).map((group) => (
                    <Dropdown className={styles.toolsButton}>
                        <Dropdown.Toggle id="dropdown-basic">{group}</Dropdown.Toggle>
                        <Dropdown.Menu>
                            {groupedOperators[group].map((item) => (
                                <Dropdown.Item href="#/action-1" onClick={() => addOperator(item.id)}>
                                    {item.title}
                                </Dropdown.Item>
                            ))}
                        </Dropdown.Menu>
                    </Dropdown>
                ))}
                <Button className={styles.toolsButton} onClick={addVariable}>Переменная</Button>
                <button onClick={dump}>Serialize</button>
            </div>

            {engine && <CanvasWidget className={styles.wrapper} engine={engine}/>}

        </div>
    )
}

export default DataProcessingView;
