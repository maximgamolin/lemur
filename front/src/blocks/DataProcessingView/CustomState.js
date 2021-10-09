import { Action, DragCanvasState, InputType, SelectingState, State } from "@projectstorm/react-canvas-core";
import { DragDiagramItemsState, PortModel } from "@projectstorm/react-diagrams-core";

export class CreateLinkState extends State {
	sourcePort;
	link;

	constructor() {
		super({ name: 'create-new-link' });

		this.registerAction(
			new Action({
				type: InputType.MOUSE_UP,
				fire: (actionEvent) => {
					const element = this.engine.getActionEventBus().getModelForEvent(actionEvent);
					const {
						event: { clientX, clientY }
					} = actionEvent;
					const ox = this.engine.getModel().getOffsetX();
					const oy = this.engine.getModel().getOffsetY();

					if (element instanceof PortModel && !this.sourcePort) {
						this.sourcePort = element;

						const link = this.sourcePort.createLinkModel();
						link.setSourcePort(this.sourcePort);
						// link.getFirstPoint().setPosition(clientX - ox, clientY - oy);
						link.getLastPoint().setPosition(clientX - ox + 20, clientY - oy + 20);

						this.link = this.engine.getModel().addLink(link);
					} else if (element instanceof PortModel && this.sourcePort && element != this.sourcePort) {
						if (this.sourcePort.canLinkToPort(element)) {
							this.link.setTargetPort(element);
							element.reportPosition();
							this.clearState();
							this.eject();
						}
					} else if (element === this.link.getLastPoint()) {
						this.link.point(clientX - ox, clientY - oy, -1);
					}

					if (element && this.sourcePort) {
						console.log(`from ${this.sourcePort.parent.options.name}(${this.sourcePort.options.name})`);
						console.log(`to ${element.parent.options.name}(${element.options.name})`);
					}
					console.log(`from: ${this.sourcePort} to: ${element}`);
					// console.log(element);
					this.engine.repaintCanvas();
				}
			})
		);

		this.registerAction(
			new Action({
				type: InputType.MOUSE_MOVE,
				fire: (actionEvent) => {
					if (!this.link) return;
					const { event } = actionEvent;
					// console.log(event);
					this.link.getLastPoint().setPosition(event.movementX, event.movementY);
					this.engine.repaintCanvas();
				}
			})
		);

		this.registerAction(
			new Action({
				type: InputType.KEY_UP,
				fire: (actionEvent) => {
					// on esc press remove any started link and pop back to default state
					if (actionEvent.event.keyCode === 27) {
						this.link.remove();
						this.clearState();
						this.eject();
						this.engine.repaintCanvas();
					}
				}
			})
		);
	}

	clearState() {
		this.link = undefined;
		this.sourcePort = undefined;
	}
}

export class DefaultState extends State {
	dragCanvas;
	createLink;
	dragItems;

	constructor() {
		super({ name: 'starting-state' });
		this.childStates = [new SelectingState()];
		this.dragCanvas = new DragCanvasState();
		this.createLink = new CreateLinkState();
		this.dragItems = new DragDiagramItemsState();

		// determine what was clicked on
		this.registerAction(
			new Action({
				type: InputType.MOUSE_DOWN,
				fire: (event) => {
					const element = this.engine.getActionEventBus().getModelForEvent(event);

					// the canvas was clicked on, transition to the dragging canvas state
					if (!element) {
						this.transitionWithEvent(this.dragCanvas, event);
					}
					// initiate dragging a new link
					else if (element instanceof PortModel) {
						return;
					}
					// move the items (and potentially link points)
					else {
						this.transitionWithEvent(this.dragItems, event);
					}
				}
			})
		);

		// touch drags the canvas
		this.registerAction(
			new Action({
				type: InputType.TOUCH_START,
				fire: (event) => {
					this.transitionWithEvent(new DragCanvasState(), event);
				}
			})
		);

		this.registerAction(
			new Action({
				type: InputType.MOUSE_UP,
				fire: (event) => {
					const element = this.engine.getActionEventBus().getModelForEvent(event);

					if (element instanceof PortModel) this.transitionWithEvent(this.createLink, event);
				}
			})
		);
	}
}

export default DefaultState;
