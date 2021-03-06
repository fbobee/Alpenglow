#ifndef INITIALIZABLE_H
#define INITIALIZABLE_H

//SIP_AUTOCONVERT

class Initializable {
/**
    This interface signals that the implementing class has to be initialized by the experiment runner. The experiment runner calls the :py:meth:`initialize()` method, which in return calls the class-specific implementation of :py:meth:`autocalled_initialize()` and sets the :py:meth:`is_initialized` flag if the initialization was successful. The :py:meth:`autocalled_initialize()` method can check whether the neccessary dependencies have been initialized or not before initializing the instance; and should return the success value accordingly.

    If the initialization was not successful, the experiment runner keeps trying to initialize the not-yet initialized objects, thus resolving dependency chains.

    Initializing and inheritance. Assume that class Parent implements Initializable, and the descendant Child needs further initialization.
    In that case Child has to override :py:meth:`autocalled_initialize()`, and call `Parent::autocalled_initialize()` in the overriding function first, continuing only if the parent returned true.
    If the init of the parent was succesful, but the children failed, then the children has to store the success of the parent and omit calling the initialization of the parent later.
*/
public:
  bool is_initialized() const { return is_initialized_; }
/**
      Returns
      -------
      bool
          Whether the component has already been initialized.
*/
  bool initialize(){
    if(!is_initialized()){
      is_initialized_ = autocalled_initialize();
      return is_initialized_;
    } else {
      return true;
    }
  }
/**
      Returns
      -------
      bool
          Whether the initialization was successful.
*/
protected:
  virtual bool autocalled_initialize()=0;
private:
  bool is_initialized_=false;
/**
      Has to be implemented by the component.

      Returns
      -------
      bool
          Whether the initialization was successful.
*/
};

#endif /* INITIALIZABLE_H */
