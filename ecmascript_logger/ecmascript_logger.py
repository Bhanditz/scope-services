# OpProtoc
from opprotoc.proto import Proto, Quantifier, Field, Message, Request, Event, Service, Options

# Service: EcmascriptLogger
# Is this service even used, and does it even work?
esl_new_script = Message("ScriptInfo",
                         fields=[Field(Proto.String, "context", 1)
                                ,Field(Proto.String, "url",     2)
                                ,Field(Proto.String, "source",  3)
                                ])

esl_configure = Message("Config",
                        fields=[Field(Proto.Bool, "reformat", 1, q=Quantifier.Optional)
                               ])

ecmascript_logger = Service("EcmascriptLogger",
                            commands=[Request(1, "Configure", esl_configure, False)
                                     ,Event(2,   "OnNewScript", esl_new_script)
                                     ],
                            options=Options(version="2.0", core_release="2.4",
                                            cpp_class="OpScopeEcmascriptLogger", cpp_hfile="modules/scope/src/scope_ecmascript_logger.h"))
