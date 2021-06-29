from app.libs.exception_lib import DeveloperException


class ModelSetRequiredFieldException(DeveloperException):
    pass


def set_property_on_model(model_instance, data: dict, property_name: str, required=True) -> None:
    original_data = None

    if property_name in data:
        original_data = getattr(model_instance, property_name)
        setattr(model_instance, property_name, data[property_name])

    if required and not getattr(model_instance, property_name):
        # put original data back
        if original_data:
            setattr(model_instance, property_name, original_data)
        raise ModelSetRequiredFieldException('"{}" is a required field'.format(property_name))
