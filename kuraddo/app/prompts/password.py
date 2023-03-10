from typing import Any
from typing import Optional

from main import Style
from main.constants.constants import DEFAULT_QUESTION_PREFIX
from main.prompts import text
from main.model.question import Question

def password(
  message: str,
  default: str = "",
  validate: Any = None,
  qmark: str = DEFAULT_QUESTION_PREFIX,
  style: Optional[Style] = None,
  **kwargs: Any,
) -> Question:
  """A text input where a user can enter a secret which won't be displayed on the CLI.
  
  This question type can be used to prompt the user for information
  that should not be shown in the command line. The typed text will be
  replaced with ``*``.

  Args:
      message: Question text.

      default: Default value will be returned if the user just hits
               enter.
      
      validate: Require the entered value to pass a validation. The 
                value can not be submitted until the validator accepts
                it (e.g. to check minimum password length).

                This can either be a function acceting the input and
                returning a boolean, or an class reference to a
                subclass of the prompt toolkit Validator class.
      
      qmark: Question prefix displayed in front of the question.
             By default this is a ``?``.

      style: A custom color and style for the question parts. You can
             configure colors as well as font types for different elements.
  Returns:
      :class:`Questions`: Question instance, ready to be prompted (using ``.ask()``).
  """

  return text.text(
    message,
    default,
    validate,
    qmark,
    style,
    is_password=True,
    **kwargs
  )