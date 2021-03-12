#!/usr/bin/env python

from twisted.internet import protocol, reactor
from time import ctime

PORT = 21567

class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print '...connected from:', clnt

    def dataReceived(self, data):
        self.transport.write('[%s] %s' % (ctime(), data))

factory = protocol.Factory()
factory.protocol = TSServProtocol
print 'waiting for connection...'
reactor.listenTCP(PORT, factory)
reactor.run()
<button name="channel" type="button" class="btn btn-menu ng-valid ng-scope ng-not-empty ng-dirty ng-valid-parse ng-touched" style="position: relative; width: 100%; overflow: hidden; text-overflow: ellipsis; padding-right: 20px;" data-html="1" data-multiple="1" data-key-en="" data-auto-close="1" data-animation="am-slide-bottom" bs-on-before-show="onBeforeShow" bs-on-before-hide="onHide" bs-on-show="onShow" ng-disabled="disabled()" data-template-url="/com/xly/iufo/static/dist/components/common/directives/partials/multiple_select.html?version=1614913043007" data-target="#1614913103581-54491" ng-model="model" bs-select="" data-placeholder="请选择" data-max-length-html="个已选" data-trigger="click" ng-class="{'error':isOverLimit}" bs-options="item.value as item.label for item in options" ng-style="{'border-color': isOverLimit ? '#f00': ''}">false, 未分类, dfdfdfdfdf&nbsp;<span class="caret"></span></button>