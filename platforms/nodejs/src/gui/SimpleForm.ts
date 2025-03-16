export interface SimpleForm {
    /**
     * Set the title of the form.
     * @param title - Title of the form
     * @returns The processed form object (for other operations in the chain)
     */
    setTitle(title: string): SimpleForm;

    /**
     * Set the content of the form.
     * @param content - Text content of the form
     * @returns The processed form object (for other operations in the chain)
     */
    setContent(content: string): SimpleForm;

    /**
     * Add a row of buttons to the form.
     * @param text - String of button text
     * @param image - The path where the button image is located (optional)
     * @returns The processed form object (for other operations in the chain)
     */
    addButton(text: string, image?: string): SimpleForm;
}
