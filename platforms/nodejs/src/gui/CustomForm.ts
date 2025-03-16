export interface CustomForm {
    /**
     * Set the title of the form.
     * @param title - Title of the form
     * @returns The processed form object (for other operations in the chain)
     */
    setTitle(title: string): CustomForm;

    /**
     * Add a line of text to the form.
     * @param text - Line of text
     * @returns The processed form object (for other operations in the chain)
     */
    addLabel(text: string): CustomForm;

    /**
     * Add a row of input boxes to the form.
     * @param title - Description text in an input box
     * @param placeholder - The default prompt in the input box (optional)
     * @param _default - The default input in the input box (optional)
     * @returns The processed form object (for other operations in the chain)
     */
    addInput(title: string, placeholder?: string, _default?: string): CustomForm;

    /**
     * Add a row of switch options to the form.
     * @param title - Description text for a switch option
     * @param _default - Default state of the switch on/off (optional)
     * @returns The processed form object (for other operations in the chain)
     */
    addSwitch(title: string, _default?: boolean): CustomForm;

    /**
     * Add a drop-down menu to the form.
     * @param title - Description text for a drop-down menu
     * @param items - List of option texts in the drop-down menu
     * @param _default - The number of the list item selected by default in the drop-down menu (optional)
     * @defaultValue 0 (first item)
     * @returns The processed form object (for other operations in the chain)
     */
    addDropdown(title: string, items: Array<string>, _default?: number): CustomForm;

    /**
     * Add a row of cursor sliders to the form.
     * @param title - Description text for a slider
     * @param min - Slider minimum value
     * @param max - Slider maximum value
     * @param step - The minimum division value of the cursor slider adjustment (optional)
     * @defaultValue 1
     * @param _default - The default initial grid number of the cursor slider, the value must be between the minimum and maximum grid number (optional)
     * @defaultValue 0 (i.e. the slider is at the beginning of the slider row)
     * @returns The processed form object (for other operations in the chain)
     */
    addSlider(title: string, min: number, max: number, step?: number, _default?: number): CustomForm;

    /**
     * Add a row of step sliders to the form.
     * @param title - Description text for a step slider
     * @param items - List of option texts for the step slider
     * @param _default - Default initial options for step sliders (optional)
     * @defaultValue 0 (i.e. the slider is at the beginning of the slider row)
     * @returns The processed form object (for other operations in the chain)
     */
    addStepSlider(title: string, items: Array<string>, _default?: number): CustomForm;
}
