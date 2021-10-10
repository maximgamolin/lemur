import React from "react";
import { useHistory } from "react-router-dom";
import {
  unstable_useFormState as useFormState,
  unstable_Form as Form,
  unstable_FormLabel as FormLabel,
  unstable_FormInput as FormInput,
  unstable_FormMessage as FormMessage,
  unstable_FormSubmitButton as FormSubmitButton,
} from "reakit/Form";
import toast from 'react-hot-toast';
import Stages from "../../../blocks/Stages";
import { connect } from "redux-zero/react";
import actions from "../../../redux/actions";


function CreateSelection({ initWorkpiece, ...rest }) {
    const history = useHistory();
    const form = useFormState({
        values: { name: '' },
        onValidate: (values) => {
            if (!values.name) {
                const errors = {
                    name: "Нужно заполнить название",
                };
                throw errors;
            }
        },
        onSubmit: async (values) => {
            initWorkpiece(values.name)
                .then(() => {
                    history.push('/collections/prepare/');
                    toast.success('Выборка создана!');
                });
        },
    });



    return (
        <>
            <Stages stages={['Создание нового датасета', 'Подготовка выборки', 'Объединение выборок', 'Экспорт']}
                    activeNum={0} />

            <Form style={{ marginTop: '32px' }} {...form}>
                <FormLabel {...form} name="name">Названия новой выборки</FormLabel>
                <FormInput {...form} name="name" placeholder="Новая выборка"/>
                <FormMessage {...form} name="name"/>
                <FormSubmitButton {...form}>Далее</FormSubmitButton>
            </Form>
        </>
    )
}

const mapToProps = ({availableTags, allDatasets}) => ({availableTags, allDatasets});

export default connect(mapToProps, actions)(CreateSelection);
