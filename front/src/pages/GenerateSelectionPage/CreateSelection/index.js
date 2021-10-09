import React from "react";
import {
  unstable_useFormState as useFormState,
  unstable_Form as Form,
  unstable_FormLabel as FormLabel,
  unstable_FormInput as FormInput,
  unstable_FormMessage as FormMessage,
  unstable_FormSubmitButton as FormSubmitButton,
} from "reakit/Form";
import { Input } from "reakit/Input";
import Heading from "../../../typography/Heading";


function CreateSelection({ ...rest }) {
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
        onSubmit: (values) => {
            alert(JSON.stringify(values, null, 2));
        },
    });

    return (
        <>
            <Heading size="h1">Создание нового датасета</Heading>

            <Form style={{ marginTop: '32px' }} {...form}>
                <FormLabel {...form} name="name">Названия новой выборки</FormLabel>
                <FormInput {...form} name="name" placeholder="Новая выборка"/>
                <FormMessage {...form} name="name"/>
                <FormSubmitButton {...form}>Далее</FormSubmitButton>
            </Form>
        </>
    )
}

export default CreateSelection;
